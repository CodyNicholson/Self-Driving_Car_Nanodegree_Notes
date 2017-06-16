# Kalman Filter Equations In C++

Now, let's do a quick refresher of the Kalman Filter for a simple 1D motion case. Let's say that your goal is to track a pedestrian with state x that is described by a position and velocity.

```
x=(p)
  (v)
```

### Prediction Step

When designing the Kalman filter, we have to define the two linear functions: the state transition function and the measurement function. The state transition function is:

**x_i = F * x + noise**

where,

```
F = (1, delta(t))
    (0, 1       )
```

and **x_i** is where we predict the object to be after time **delta(t)**

**F** is a matrix that, when multiplied with **x**, predicts where the object will be after time **delta(t)**.

By using the linear motion model with a constant velocity, the new location, **p_i** is calculated as:

p_i = p + v * delta(t)

where **p** is the old location and **v**, the velocity, will be the same as the new velocity (v_i = v) because the velocity is constant.

We can express this in a matrix form as follows

```
(p_i) = (1, delta(t))(p)
(v_i) = (0, 1       )(v)
```

Remember we are representing the object location and velocity as gaussian distributions with mean **x**. When working with the equation **x_i = Fx + noise**, we are calculating the mean value of the state vector. The noise is also represented by a gaussian distribution but with mean zero; hence, noise = 0 is saying that the mean noise is zero. The update equation then becomes x_i = Fx

But the noise does have uncertainty. The uncertainty shows up in the Q matrix as acceleration noise.

### Update Step

For the update step, we use the measurement function to map the state vector into the measurement space of the sensor. To give a concrete example, lidar only measures an object's position. But the extended Kalman filter models an object's position and velocity. So multiplying by the measurement function H matrix will drop the velocity information from the state vector **x**. Then the lidar measurement position and our belief about the object's position can be compared.

```
z = H * x + w
```

where **w** represents sensor measurement noise.

So for lidar, the measurement function looks like this:

z = p_i

It also can be represented in a matrix form:

```
z = (1, 0) (p_i)
           (v_i)
```

As we already know, the general algorithm is composed of a prediction step where I predict the new state and covariance, **P**.

And we also have a measurement update (or also called many times a correction step) where we use the latest measurements to update our estimate and our uncertainty.

***

### Code For C++ Kalman Filter

```c++
// Write a function 'filter()' that implements a multi-
// dimensional Kalman Filter for the example given
//============================================================================
#include <iostream>
#include "Dense"
#include <vector>

using namespace std;
using namespace Eigen;

//Kalman Filter variables
VectorXd x; // object state
MatrixXd P; // object covariance matrix
VectorXd u; // external motion
MatrixXd F; // state transition matrix
MatrixXd H; // measurement matrix
MatrixXd R; // measurement covariance matrix
MatrixXd I; // Identity matrix
MatrixXd Q; // process covariance matrix

vector<VectorXd> measurements;
void filter(VectorXd &x, MatrixXd &P);


int main() {
    /**
     * Code used as example to work with Eigen matrices
     */
//  //you can create a  vertical vector of two elements with a command like this
//  VectorXd my_vector(2);
//  //you can use the so called comma initializer to set all the coefficients to some values
//  my_vector << 10, 20;
//
//
//  //and you can use the cout command to print out the vector
//  cout << my_vector << endl;
//
//
//  //the matrices can be created in the same way.
//  //For example, This is an initialization of a 2 by 2 matrix
//  //with the values 1, 2, 3, and 4
//  MatrixXd my_matrix(2,2);
//  my_matrix << 1, 2,
//          3, 4;
//  cout << my_matrix << endl;
//
//
//  //you can use the same comma initializer or you can set each matrix value explicitly
//  // For example that's how we can change the matrix elements in the second row
//  my_matrix(1,0) = 11;    //second row, first column
//  my_matrix(1,1) = 12;    //second row, second column
//  cout << my_matrix << endl;
//
//
//  //Also, you can compute the transpose of a matrix with the following command
//  MatrixXd my_matrix_t = my_matrix.transpose();
//  cout << my_matrix_t << endl;
//
//
//  //And here is how you can get the matrix inverse
//  MatrixXd my_matrix_i = my_matrix.inverse();
//  cout << my_matrix_i << endl;
//
//
//  //For multiplying the matrix m with the vector b you can write this in one line as let’s say matrix c equals m times v.
//  //
//  MatrixXd another_matrix;
//  another_matrix = my_matrix*my_vector;
//  cout << another_matrix << endl;


    //design the KF with 1D motion
    x = VectorXd(2);
    x << 0, 0;

    P = MatrixXd(2, 2);
    P << 1000, 0, 0, 1000;

    u = VectorXd(2);
    u << 0, 0;

    F = MatrixXd(2, 2);
    F << 1, 1, 0, 1;

    H = MatrixXd(1, 2);
    H << 1, 0;

    R = MatrixXd(1, 1);
    R << 1;

    I = MatrixXd::Identity(2, 2);

    Q = MatrixXd(2, 2);
    Q << 0, 0, 0, 0;

    //create a list of measurements
    VectorXd single_meas(1);
    single_meas << 1;
    measurements.push_back(single_meas);
    single_meas << 2;
    measurements.push_back(single_meas);
    single_meas << 3;
    measurements.push_back(single_meas);

    //call Kalman filter algorithm
    filter(x, P);

    return 0;

}


void filter(VectorXd &x, MatrixXd &P) {

    for (unsigned int n = 0; n < measurements.size(); ++n) {

        VectorXd z = measurements[n];
        //YOUR CODE HERE
        /*
         * KF Measurement update step
         */
        VectorXd y = z - H * x; // Error calculation given new measurement z
        MatrixXd Ht = H.transpose();
        MatrixXd S = H * P * Ht + R;
        MatrixXd Si = S.inverse();
        MatrixXd K =  P * Ht * Si; // Gain

        // new updated state: x, and variance: p
        x = x + (K * y);
        P = (I - K * H) * P;

        /*
         * KF Prediction step
         */
        x = F * x + u;
        MatrixXd Ft = F.transpose();
        P = F * P * Ft + Q;

        std::cout << "x=" << std::endl <<  x << std::endl;
        std::cout << "P=" << std::endl <<  P << std::endl;


    }
}
```

Why do we not use the process noise in the state prediction function, even though the state transition equation has one? In other words, why does the code set u << 0, 0 for the equation x = F * x + u?

Looking closely at the process noise, we know from the Kalman Filter algorithm that its mean is zero and its covariance matrix is usually noted by Q * N(0,Q). The first equation only predicts the mean state. As the mean value of the noise is zero, it does not directly affect the predicted state. However, we can see that the noise covariance Q is added here to the state covariance prediction so that the state uncertainty always increases through the process noise.

