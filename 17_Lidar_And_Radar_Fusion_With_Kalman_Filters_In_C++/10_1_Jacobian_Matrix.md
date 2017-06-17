# Jacobian Matrix

We have to linearize our function **h(x)**. This starts with derivatives. If we generalize to a higher dimensionality, the derivative of **h(x)** with respect to x is called the **Jacobian**.

The **Jacobian** is a matrix containing all the partial derivatives. We know the measurement function describes: **range, bearing, and range rate**. The state vector has four components: **Px, Py, Vx, Vy**.

In this case, the Jacobian matrix **Hj** is going to be a matrix with three rows and four columns.

## Code

```c++
#include <iostream>
#include "Dense"
#include <vector>

using namespace std;
using Eigen::MatrixXd;
using Eigen::VectorXd;

MatrixXd CalculateJacobian(const VectorXd& x_state);

int main() {

    /*
     * Compute the Jacobian Matrix
     */

    //predicted state  example
    //px = 1, py = 2, vx = 0.2, vy = 0.4
    VectorXd x_predicted(4);
    x_predicted << 1, 2, 0.2, 0.4;

    MatrixXd Hj = CalculateJacobian(x_predicted);

    cout << "Hj:" << endl << Hj << endl;

    return 0;
}

MatrixXd CalculateJacobian(const VectorXd& x_state) {
    
    // Declare matrix
    MatrixXd Hj(3,4);
    
    // Use the predicted state to get the four state parameters
    float px = x_state(0);
    float py = x_state(1);
    float vx = x_state(2);
    float vy = x_state(3);

    // Use that state parameters to compute each Jacobian element
    // according to the matrix definition
    // We precompute some of the terms to make it cleaner code
    float c1 = px*px+py*py;
    float c2 = sqrt(c1);
    float c3 = (c1*c2);

    // Check division by zero
    if(fabs(c1) < 0.0001){
        cout << "CalculateJacobian () - Error - Division by Zero" << endl;
        return Hj;
    }

    // Compute the Jacobian matrix
    Hj << (px/c2), (py/c2), 0, 0,
          -(py/c1), (px/c1), 0, 0,
          py*(vx*py - vy*px)/c3, px*(px*vy - py*vx)/c3, px/c2, py/c2;

    return Hj;
}
```
