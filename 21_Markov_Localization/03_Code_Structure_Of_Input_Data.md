# Code Structure Of Input Data

main.cpp:

```c++
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include "measurement_package.h"
#include "map.h"
#include "help_functions.h"

using namespace std;

int main() {
    // Declaration

    //define example: 01, 02, 03, 04
    string example_string = "01";

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


    // read map and  measurements:

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

    // Coding quiz 1: just print out map infos and measurement package:
    
    std::cout <<"..................................................."<< std::endl;
    std::cout <<"..................................................."<< std::endl;
    std::cout <<"............----> Coding quiz 1  <----............."<< std::endl;
    std::cout <<"..................................................."<< std::endl;
    std::cout <<"..................................................."<< std::endl;
       
    //print out map:
    std::cout << "Print out the map landmarks:" << endl;
    

    for(int i=0;i<map_1d.landmark_list.size();i++){
        std::cout << "ID: "<< map_1d.landmark_list[i].id_i << "\t"
                  << "value in x: " << map_1d.landmark_list[i].x_f << std::endl;
    }
    std::cout << "..................................................." << std::endl;
    std::cout << "..................................................." << std::endl;

    //print out the controls and the observations:
    std::cout << "Print out the measurement packages:" << endl;

        for(int i=0;i<measurement_pack_list.size();i++){

            std::cout << "Step "<< i << " includes the move " 
                      << measurement_pack_list[i].control_s_.delta_x_f 
                      <<  "[m] in driving direction " << std::endl;

            //run over observations:
            if (measurement_pack_list[i].observation_s_.distance_f.size()<1){

                std::cout<< "   No observations in step "<< i << std::endl;
            }
            else{
                std::cout<< "   Number of Observations in current step: "
                         << measurement_pack_list[i].observation_s_.distance_f.size() 
                         << std::endl;
                
                for(int j=0;j<measurement_pack_list[i].observation_s_.distance_f.size();j++ ){
                    std::cout<< "   Distance to a landmark: "
                             <<  measurement_pack_list[i].observation_s_.distance_f[j]
                             <<  " m" <<std::endl;
                }
            }
            std::cout << "..................................................."<< std::endl;
        }
    return 0;
}
```

help_functions.h:

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
        std::cout << std::fixed << std::setprecision(5)<< "sqrt error sum:     " << "\t" << sqrt((error_sum)) <<std::endl;
        std::cout <<"..................................................."<< std::endl;
        std::cout <<"..................................................."<< std::endl;
        return true;

    }
};
#endif /* HELP_FUNCTIONS_H_ */
```

measurement_package:

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

map.h:

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
