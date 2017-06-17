# Evaluating Kalman Filter Performance

Once we have implemented the tracking algorithm, we should check its performance in terms of how fat the estimated result is from the true result. There are many evaluation metrics, but the most common one is the **root mean squared error**.

In the context of tracking, it's an accuracy metric used to measure the deviation of the estimated state from the true state.

At the given processing step, I need two values: The estimated state which is a vector with a position and velocity components, and the real values that are usually known as ground truth values. The difference between the estimated state and the ground truth state gives us the **residual**. These residuals are then squared and averaged, and the square root gives us the error metric.

The lower is the error, and the higher is the estimation accuracy

***

## Code

```c++
#include <iostream>
#include "Dense"
#include <vector>

using namespace std;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::vector;

VectorXd CalculateRMSE(const vector<VectorXd> &estimations,
        const vector<VectorXd> &ground_truth);

int main() {
    /*
     * Compute RMSE
     */
    vector<VectorXd> estimations;
    vector<VectorXd> ground_truth;

    //the input list of estimations
    VectorXd e(4);
    e << 1, 1, 0.2, 0.1;
    estimations.push_back(e);
    e << 2, 2, 0.3, 0.2;
    estimations.push_back(e);
    e << 3, 3, 0.4, 0.3;
    estimations.push_back(e);

    //the corresponding list of ground truth values
    VectorXd g(4);
    g << 1.1, 1.1, 0.3, 0.2;
    ground_truth.push_back(g);
    g << 2.1, 2.1, 0.4, 0.3;
    ground_truth.push_back(g);
    g << 3.1, 3.1, 0.5, 0.4;
    ground_truth.push_back(g);

    //call the CalculateRMSE and print out the result
    cout << CalculateRMSE(estimations, ground_truth) << endl;


    return 0;
}

VectorXd CalculateRMSE(const vector<VectorXd> &estimations,
        const vector<VectorXd> &ground_truth){

    VectorXd rmse(4);
    rmse << 0,0,0,0;

    // check the validity of the following inputs:
    //  * the estimation vector size should not be zero
    //  * the estimation vector size should equal ground truth vector size
    if(estimations.size() != ground_truth.size()
            || estimations.size() == 0){
        cout << "Invalid estimation or ground_truth data" << endl;
        return rmse;
    }

    //accumulate squared residuals
    for(unsigned int i=0; i < estimations.size(); ++i){

        VectorXd residual = estimations[i] - ground_truth[i];

        //coefficient-wise multiplication
        residual = residual.array()*residual.array();
        rmse += residual;
    }

    //calculate the mean
    rmse = rmse/estimations.size();

    //calculate the squared root
    rmse = rmse.array().sqrt();

    //return the result
    return rmse;
}
```
