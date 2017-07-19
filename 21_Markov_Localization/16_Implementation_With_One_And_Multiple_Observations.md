# Implementation With One & Multiple Observations

bayesianFilter.cpp

```c++
#include "bayesianFilter.h"
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//constructor:
bayesianFilter::bayesianFilter() {

    //set initialization to false:
    is_initialized_ = false;

    //set standard deviation of control:
    control_std     = 1.0f;

    //set standard deviation of observations:
    observation_std = 1.0f;
    
    //define size of different state vectors:
    bel_x.resize(100,0);
    bel_x_init.resize(100,0);

}

//de-constructor:
bayesianFilter::~bayesianFilter() {

}

void bayesianFilter::process_measurement(const MeasurementPackage &measurements,
                                             const map &map_1d,
                                         help_functions &helpers){

    /******************************************************************************
     *  Set init belief of state vector:
     ******************************************************************************/
    if(!is_initialized_){

        //run over map:
        for (unsigned int l=0; l< map_1d.landmark_list.size(); ++l){

            //define landmark:
            map::single_landmark_s landmark_temp;
            //get landmark from map:
            landmark_temp = map_1d.landmark_list[l];

            //check, if landmark position is in the range of state vector x:
            if(landmark_temp.x_f > 0 && landmark_temp.x_f < bel_x_init.size() ){

                //cast float to int:
                int position_x = int(landmark_temp.x_f) ;
                //set belief to 1:
                bel_x_init[position_x]   = 1.0f;
                bel_x_init[position_x-1] = 1.0f;
                bel_x_init[position_x+1] = 1.0f;

            } //end if
        }//end for

    //normalize belief at time 0:
    bel_x_init = helpers.normalize_vector(bel_x_init);

    //set initial flag to true:
    is_initialized_ = true ;
    
    }//end if


    /******************************************************************************
     *  motion model and observation update
    ******************************************************************************/
    std::cout <<"-->motion model for state x ! \n" << std::endl;

    //get current observations and control information:
    MeasurementPackage::control_s     controls = measurements.control_s_;
    MeasurementPackage::observation_s observations = measurements.observation_s_;

    //run over the whole state (index represents the pose in x!):
    for (unsigned int i=0; i< bel_x.size(); ++i){


        float pose_i = float(i) ;
        /**************************************************************************
         *  posterior for motion model
        **************************************************************************/

        // motion posterior:
        float posterior_motion = 0.0f;

        //loop over state space x_t-1 (convolution):
        for (unsigned int j=0; j< bel_x.size(); ++j){
            float pose_j = float(j) ;
            
            
            float distance_ij = pose_i-pose_j;

            //transition probabilities:
            float transition_prob = helpers.normpdf(distance_ij,
                                                    controls.delta_x_f,
                                                    control_std) ;
            //motion model:
            posterior_motion += transition_prob*bel_x_init[j];
        }

        /**************************************************************************
         *  observation update:
        **************************************************************************/
            
        //define pseudo observation vector:
        std::vector<float> pseudo_ranges ;

        //define maximum distance:
        float distance_max = 100;
            
        //loop over number of landmarks and estimate pseudo ranges:
        for (unsigned int l=0; l< map_1d.landmark_list.size(); ++l){

            //estimate pseudo range for each single landmark 
            //and the current state position pose_i:
            float range_l = map_1d.landmark_list[l].x_f - pose_i;
            
            //check, if distances are positive: 
            if(range_l > 0.0f)
            pseudo_ranges.push_back(range_l) ;
        }

        //sort pseudo range vector:
        sort(pseudo_ranges.begin(), pseudo_ranges.end());

        //define observation posterior:
        float posterior_obs = 1.0f ;
        
        //run over current observation vector:
        for (unsigned int z=0; z< observations.distance_f.size(); ++z){

            //define min distance:
            float pseudo_range_min;

            //check, if distance vector exists:
            if(pseudo_ranges.size() > 0){

                //set min distance:
                pseudo_range_min = pseudo_ranges[0];
                //remove this entry from pseudo_ranges-vector:
                pseudo_ranges.erase(pseudo_ranges.begin());

            }
            //no or negative distances: set min distance to maximum distance:
            else{
                pseudo_range_min = distance_max ;
            }

            //estimate the posterior for observation model: 
            posterior_obs*= helpers.normpdf(observations.distance_f[z], 
                                            pseudo_range_min,
                                            observation_std); 
        }
        
        /**************************************************************************
         *  finalize bayesian localization filter:
         *************************************************************************/
        
        //update = observation_update* motion_model
        bel_x[i] = posterior_obs*posterior_motion ;

    }; 

    //normalize:
    bel_x = helpers.normalize_vector(bel_x);

    //set bel_x to belief_init:
    bel_x_init = bel_x;
};
```

main.cpp

```c++
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include "measurement_package.h"
#include "map.h"
#include "help_functions.h"

#include "bayesianFilter.h"
using namespace std;

int main() {

    /******************************************************************************
     *  declaration:                                                                  
     *****************************************************************************/
    
    //define example: 01, 02, 03, 04
    string example_string = "04";

    //declare map:
    map map_1d;

    //declare measurement list:
    std::vector<MeasurementPackage> measurement_pack_list;

    //declare helpers:
    help_functions helper;

    //define file names:
    char in_file_name_ctr[1024];
    char in_file_name_obs[1024];
    char in_file_name_gt[1024];

    /******************************************************************************
     *  read map and measurements:                                               *
     *****************************************************************************/
    //read map:
    helper.read_map_data("data/map_1d.txt", map_1d);

    //define file name of controls:
    sprintf(in_file_name_ctr, "data/example%s/control_data.txt", 
            example_string.c_str());

    //define file name of observations:
    sprintf(in_file_name_obs, "data/example%s/observations/", 
            example_string.c_str());
    
    //read in data to measurement package list:
    helper.read_measurement_data(in_file_name_ctr, 
                                 in_file_name_obs, 
                                 measurement_pack_list);

    /*******************************************************************************
     *  start 1d_bayesian filter                                                   *
     *******************************************************************************/

    //create instance of 1d_bayesian localization filter:
    bayesianFilter localization_1d_bayesian;

    //define number of time steps:
    size_t T = measurement_pack_list.size();

    //cycle:
    for (size_t t = 0; t < T; ++t){

        //Call 1d_bayesian filter:
        localization_1d_bayesian.process_measurement(measurement_pack_list[t],
                                                     map_1d,
                                                     helper);
    }

    /*******************************************************************************
     *  print/compare results:                                                 *
     ********************************************************************************/
    //define file name of gt data:
    sprintf(in_file_name_gt, "data/example%s/gt_example%s.txt",example_string.c_str(),example_string.c_str() );

    ///compare gt data with results:
    helper.compare_data(in_file_name_gt, localization_1d_bayesian.bel_x);
    

    return 0;
}
```

bayesianFilter.h

```c++
#ifndef BAYESIANFILTER_H_
#define BAYESIANFILTER_H_

#include <vector>
#include <string>
#include <fstream>

#include "measurement_package.h"
#include "map.h"
#include "help_functions.h"

class bayesianFilter {
public:
    //constructor:
    bayesianFilter();
    //deconstructor:
    virtual ~bayesianFilter();


    //main public member function, which estimate the beliefs:
    void process_measurement(const MeasurementPackage &measurements,
                             const map &map_1d,
                             help_functions &helpers);

    //member public: belief of state x:
    std::vector<float> bel_x ;

private:

/////private members:

    //flag, if filter is initialized:
    bool is_initialized_;

    //precision of control information:
    float control_std ;
    
    //precision of observations as standard deviation:
    float observation_std ;
    
    //initial belief of state x:
    std::vector<float> bel_x_init ;

};

#endif /* BAYESIANFILTER_H_ */
```

help_functions.h

```c++
#ifndef HELP_FUNCTIONS_H_
#define HELP_FUNCTIONS_H_

#include <math.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include "measurement_package.h"


class help_functions {
public:

    //definition of one over square root of 2*pi:
    float ONE_OVER_SQRT_2PI = 1/sqrt(2*M_PI) ;

    //definition square:
    float squared(float x)
    {
        return x*x;
    }

    /*****************************************************************************
     * normpdf(X,mu,sigma) computes the probability function at values x using the
     * normal distribution with mean mu and standard deviation std. x, mue and 
     * sigma must be scalar! The parameter std must be positive. 
     * The normal pdf is y=f(x;mu,std)= 1/(std*sqrt(2pi)) e[ -(x−mu)^2 / 2*std^2 ]
    *****************************************************************************/
    float normpdf(float x, float mu, float std) {
        return (ONE_OVER_SQRT_2PI/std)*exp(-0.5*squared((x-mu)/std));
    }

    //function to normalize a vector:
    std::vector<float> normalize_vector(std::vector<float> inputVector){

        //declare sum:
        float sum = 0.0f;

        //declare and resize output vector:
        std::vector<float> outputVector ;
        outputVector.resize(inputVector.size());

        //estimate the sum:
        for (unsigned int i = 0; i < inputVector.size(); ++i) {
            sum += inputVector[i];
        }

        //normalize with sum:
        for (unsigned int i = 0; i < inputVector.size(); ++i) {
            outputVector[i] = inputVector[i]/sum ;
        }

        //return normalized vector:
        return outputVector ;
    }


    /* Reads map data from a file.
     * @param filename Name of file containing map data.
     */
    inline bool read_map_data(std::string filename, map& map) {

        // Get file of map:
        std::ifstream in_file_map(filename.c_str(),std::ifstream::in);
        // Return if we can't open the file.
        if (!in_file_map) {
            return false;
        }

        //declare single line of map file:
        std::string line_map;

        //run over each single line:
        while(getline(in_file_map, line_map)){

            std::istringstream iss_map(line_map);

            //declare landmark values and ID:
            float landmark_x_f;
            int id_i;

            //read data from current line to values::
            iss_map >> id_i ;
            iss_map >> landmark_x_f ;


            //declare single_landmark:
            map::single_landmark_s single_landmark_temp ;

            //set values
            single_landmark_temp.id_i = id_i ;
            single_landmark_temp.x_f  = landmark_x_f;

            //push_back in landmark list of map_1d:
            map.landmark_list.push_back(single_landmark_temp);

        }
        return true;
    }


    /* Reads measurements from a file.
     * @param filename Name of file containing measurement  data.
     */
    inline bool read_measurement_data(std::string filename_control,
                                      std::string filename_obs,
                                      std::vector<MeasurementPackage>& measurement_pack_list) {
    //get file of measurements:
    std::ifstream in_file_control(filename_control.c_str(),std::ifstream::in);
    if (!in_file_control) {
        return false;
    }
    //declare single line of measurement file:
    std::string line;

    int count = 1 ;

    //run over each single line:
    while(getline(in_file_control, line)){

        //declare measurement package:
        MeasurementPackage meas_package;

        std::istringstream iss(line);

        //declare position values:
        float delta_x_f;

        //read data from line to values:
        iss >> delta_x_f;


        //set control information:
        meas_package.control_s_.delta_x_f = delta_x_f ;

        //read observations for each control information:
        char str_obs[1024];

        //define file name of observations for current control/position info:
        sprintf(str_obs,"%sobservations_%06i.txt", filename_obs.c_str(), count);
        std::string in_file_name_observation = std::string(str_obs);


        //get file of observations:
        std::ifstream in_file_observation(in_file_name_observation.c_str(),
                                          std::ifstream::in);
        if (!in_file_observation) {
            return false;
        }

        std::string line_obs;

        //run over each single line:
        while(getline(in_file_observation, line_obs)){

            std::istringstream iss_obs(line_obs);

            //declare observation values:
            float distance_f;

            //read data from line to values:
            iss_obs >> distance_f;

            //set observation information:
            meas_package.observation_s_.distance_f.push_back(distance_f);
        }
        //push_back single package in measurement list:
        measurement_pack_list.push_back(meas_package);

        //increase counter for observation files:
        count++;
    }
    return true;
    }

    inline bool compare_data(std::string filename_gt,
                             std::vector<float>& result_vec) {
    /*****************************************************************************
     *  print/compare results:                                                 *
     *****************************************************************************/
    //get GT data:
    //define file name of map:

        std::vector<float> gt_vec;

        //get file of map:
        std::ifstream in_file_gt(filename_gt.c_str(),std::ifstream::in);

        //declare single line of map file:
        std::string line_gt;

        //run over each single line:
        while(getline(in_file_gt, line_gt)){

            std::istringstream iss_gt(line_gt);
            float gt_value;

            //read data from current line to values::
            iss_gt >> gt_value  ;
            gt_vec.push_back(gt_value);

        }
        float error_sum;
        float belief_sum;
        error_sum  = 0.0f;
        belief_sum = 0.0f;
        std::cout <<"..................................................."<< std::endl;
        std::cout <<"...............----> Results <----................."<< std::endl;
        std::cout <<"..................................................."<< std::endl;

        for (unsigned int i = 0; i <  result_vec.size(); ++i){
            error_sum+= (gt_vec[i]-result_vec[i])*(gt_vec[i]-result_vec[i]);
            belief_sum+= result_vec[i] ;
            std::cout << std::fixed << std::setprecision(5) <<"bel_x="<< i <<":" << "\t"
                      << result_vec[i]<<"\t"
                      << "ground truth:" << "\t"
                      << gt_vec[i]<<"\t" << std::endl ;
        }
        std::cout <<"..................................................."<< std::endl;
        std::cout << std::fixed << std::setprecision(5)<< "sum bel:"    << "\t" << belief_sum <<std::endl;
        std::cout <<"..................................................."<< std::endl;
        std::cout << std::fixed << std::setprecision(5)<< " rse   :     "<< "\t" << sqrt((error_sum)) <<std::endl;
        std::cout <<"..................................................."<< std::endl;
        std::cout <<"..................................................."<< std::endl;
        return true;

    }
};

#endif /* HELP_FUNCTIONS_H_ */
```

map.h

```c++
#ifndef MAP_H_
#define MAP_H_

class map {

public:
    //definition of single landmark:
    struct single_landmark_s{
        int id_i ;
        float x_f;
    };

    //list of landmarks:
    std::vector<single_landmark_s> landmark_list ;
};
#endif /* MAP_H_ */
```

measurement_package.h

```c++
#ifndef MEASUREMENT_PACKAGE_H_
#define MEASUREMENT_PACKAGE_H_
#include <vector>

class MeasurementPackage {
public:

    struct control_s{
        float delta_x_f;     // move to successor in x position
    };

    struct observation_s{
        std::vector <float> distance_f;  // distance to observed landmark
    };
    
    control_s control_s_;
    observation_s observation_s_ ;
};

#endif /* MEASUREMENT_PACKAGE_H_ */
```
