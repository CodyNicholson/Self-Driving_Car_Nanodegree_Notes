# Laser Measurement Code

For laser sensors, we have a 2D measurement vector. Each location component px, py are affected by a random noise. So our noise vector ω has the same dimension as z. And it is a distribution with zero mean and a 2 x 2 covariance matrix which comes from the product of the vertical vector ω and its transpose.

```

```

where R is the measurement noise covariance matrix; in other words, the matrix R represents the uncertainty in the position measurements we receive from the laser sensor.

Generally, the parameters for the random noise measurement matrix will be provided by the sensor manufacturer. For the extended Kalman filter project, we have provided R matrices values for both the radar sensor and the lidar sensor.

Remember that the diagonal 0s in R indicate that the noise processes are uncorrelated.

You have all you need for laser-only tracking! Now, I want you to apply what you've learned in a programming assignment.

![alt tag](imgs/helpfulEquations.png)

***

main.cpp

```c++
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include "Dense"
#include "measurement_package.h"
#include "tracking.h"

using namespace std;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::vector;


int main() {

    /*******************************************************************************
     *  Set Measurements                                                             *
     *******************************************************************************/
    vector<MeasurementPackage> measurement_pack_list;

    // hardcoded input file with laser and radar measurements
    string in_file_name_ = "obj_pose-laser-radar-synthetic-input.txt";
    ifstream in_file(in_file_name_.c_str(),std::ifstream::in);

    if (!in_file.is_open()) {
        cout << "Cannot open input file: " << in_file_name_ << endl;
    }

    string line;
    // set i to get only first 3 measurments
    int i = 0;
    while(getline(in_file, line) && (i<=3)){

        MeasurementPackage meas_package;

        istringstream iss(line);
        string sensor_type;
        iss >> sensor_type; //reads first element from the current line
        long timestamp;
        if(sensor_type.compare("L") == 0){  //laser measurement
            //read measurements
            meas_package.sensor_type_ = MeasurementPackage::LASER;
            meas_package.raw_measurements_ = VectorXd(2);
            float x;
            float y;
            iss >> x;
            iss >> y;
            meas_package.raw_measurements_ << x,y;
            iss >> timestamp;
            meas_package.timestamp_ = timestamp;
            measurement_pack_list.push_back(meas_package);

        }else if(sensor_type.compare("R") == 0){
            //Skip Radar measurements
            continue;
        }
        i++;

    }

    //Create a Tracking instance
    Tracking tracking;

    //call the ProcessingMeasurement() function for each measurement
    size_t N = measurement_pack_list.size();
    for (size_t k = 0; k < N; ++k) {    //start filtering from the second frame (the speed is unknown in the first frame)
        tracking.ProcessMeasurement(measurement_pack_list[k]);
        
    }

    if(in_file.is_open()){
        in_file.close();
    }
    return 0;
}
```

kalman_filter.cpp

```c++
#include "kalman_filter.h"

KalmanFilter::KalmanFilter() {
}

KalmanFilter::~KalmanFilter() {
}

void KalmanFilter::Predict() {
    x_ = F_ * x_;
    MatrixXd Ft = F_.transpose();
    P_ = F_ * P_ * Ft + Q_;
}

void KalmanFilter::Update(const VectorXd &z) {
    VectorXd z_pred = H_ * x_;
    VectorXd y = z - z_pred;
    MatrixXd Ht = H_.transpose();
    MatrixXd S = H_ * P_ * Ht + R_;
    MatrixXd Si = S.inverse();
    MatrixXd PHt = P_ * Ht;
    MatrixXd K = PHt * Si;

    //new estimate
    x_ = x_ + (K * y);
    long x_size = x_.size();
    MatrixXd I = MatrixXd::Identity(x_size, x_size);
    P_ = (I - K * H_) * P_;
}
```

kalman_filter.h

```c++
#ifndef KALMAN_FILTER_H_
#define KALMAN_FILTER_H_
#include "Dense"

using Eigen::MatrixXd;
using Eigen::VectorXd;

class KalmanFilter {
public:

    ///* state vector
    VectorXd x_;

    ///* state covariance matrix
    MatrixXd P_;

    ///* state transistion matrix
    MatrixXd F_;

    ///* process covariance matrix
    MatrixXd Q_;

    ///* measurement matrix
    MatrixXd H_;

    ///* measurement covariance matrix
    MatrixXd R_;

    /**
     * Constructor
     */
    KalmanFilter();

    /**
     * Destructor
     */
    virtual ~KalmanFilter();

    /**
     * Predict Predicts the state and the state covariance
     * using the process model
     */
    void Predict();

    /**
     * Updates the state and
     * @param z The measurement at k+1
     */
    void Update(const VectorXd &z);

};

#endif /* KALMAN_FILTER_H_ */
```

tracking.cpp

```c++
#include "Dense"
#include <iostream>
#include "tracking.h"

using namespace std;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::vector;

Tracking::Tracking() {
    is_initialized_ = false;
    previous_timestamp_ = 0;

    //create a 4D state vector, we don't know yet the values of the x state
    kf_.x_ = VectorXd(4);

    //state covariance matrix P
    kf_.P_ = MatrixXd(4, 4);
    kf_.P_ << 1, 0, 0, 0,
              0, 1, 0, 0,
              0, 0, 1000, 0,
              0, 0, 0, 1000;


    //measurement covariance
    kf_.R_ = MatrixXd(2, 2);
    kf_.R_ << 0.0225, 0,
              0, 0.0225;

    //measurement matrix
    kf_.H_ = MatrixXd(2, 4);
    kf_.H_ << 1, 0, 0, 0,
              0, 1, 0, 0;

    //the initial transition matrix F_
    kf_.F_ = MatrixXd(4, 4);
    kf_.F_ << 1, 0, 1, 0,
              0, 1, 0, 1,
              0, 0, 1, 0,
              0, 0, 0, 1;

    //set the acceleration noise components
    noise_ax = 5;
    noise_ay = 5;

}

Tracking::~Tracking() {

}

// Process a single measurement
void Tracking::ProcessMeasurement(const MeasurementPackage &measurement_pack) {
    if (!is_initialized_) {
        //cout << "Kalman Filter Initialization " << endl;

        //set the state with the initial location and zero velocity
        kf_.x_ << measurement_pack.raw_measurements_[0], measurement_pack.raw_measurements_[1], 0, 0;

        previous_timestamp_ = measurement_pack.timestamp_;
        is_initialized_ = true;
        return;
    }

    //compute the time elapsed between the current and previous measurements
    float dt = (measurement_pack.timestamp_ - previous_timestamp_) / 1000000.0; //dt - expressed in seconds
    previous_timestamp_ = measurement_pack.timestamp_;

    float dt_2 = dt * dt;
    float dt_3 = dt_2 * dt;
    float dt_4 = dt_3 * dt;

    //Modify the F matrix so that the time is integrated
    kf_.F_(0, 2) = dt;
    kf_.F_(1, 3) = dt;

    //set the process covariance matrix Q
    kf_.Q_ = MatrixXd(4, 4);
    kf_.Q_ <<  dt_4/4*noise_ax, 0, dt_3/2*noise_ax, 0,
               0, dt_4/4*noise_ay, 0, dt_3/2*noise_ay,
               dt_3/2*noise_ax, 0, dt_2*noise_ax, 0,
               0, dt_3/2*noise_ay, 0, dt_2*noise_ay;

    //predict
    kf_.Predict();

    //measurement update
    kf_.Update(measurement_pack.raw_measurements_);

    std::cout << "x_= " << kf_.x_ << std::endl;
    std::cout << "P_= " << kf_.P_ << std::endl;

}
```

tracking.h

```c++

#ifndef FUSION_KF_H_
#define FUSION_KF_H_

#include "measurement_package.h"
#include <vector>
#include <string>
#include <fstream>
#include "kalman_filter.h"

class Tracking {
public:
    Tracking();
    virtual ~Tracking();
    void ProcessMeasurement(const MeasurementPackage &measurement_pack);
    KalmanFilter kf_;

private:
    bool is_initialized_;
    long previous_timestamp_;

    //acceleration noise components
    float noise_ax;
    float noise_ay;

};

#endif /* FUSION_KF_H_ */
```

measurement_package.h

```c++
#ifndef MEASUREMENT_PACKAGE_H_
#define MEASUREMENT_PACKAGE_H_

#include "Dense"

class MeasurementPackage {
public:
    long timestamp_;

    enum SensorType {
        LASER, RADAR
    } sensor_type_;

    Eigen::VectorXd raw_measurements_;

};
#endif /* MEASUREMENT_PACKAGE_H_ */
```
