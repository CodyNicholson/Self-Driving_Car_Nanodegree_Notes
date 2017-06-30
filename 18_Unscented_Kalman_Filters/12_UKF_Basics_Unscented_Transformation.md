# UKF Basics: Unscented Transformation

The Unscented Kalman filter finds the mean vector and covariance matrix using **sigma points**

It can be difficult to transform the whole state distribution through a nonlinear function, but it is very easy to transform individual points of the state space through the nonlinear function, and this is what **sigma points** are for

The sigma points are chosen around the mean state and in a certain relation to the standard deviation sigma of every state direction. This is why the points are called *sigma points*. The serve as representatives of the whole distribution.

Once you have chosen the sigma points, you just insert every single sigma point into the nonlinear function **f**. The sigma points will be found somewhere in the predicted state space. Now all we have to do is calculate the mean and the covariance of your sigma points. This will not provide the same mean and covariance as the real predicted distribution, but in many cases it gives a useful approximation.

You can apply this same technique in the linear case, which is why the output will be the exact same as a EKF for a linear process model, but it calculating the sigma points takes more time so a EKF is preferred in the linear process model case

***

### Process Chain Of UKF

Starting with a state vector **x** and a covariance matrix **p**, we will go all the way through prediction and the measurement step until we reach the updated state and covariance matrix

We will start with the prediction step, which we can split into three parts for the unscented prediction:

1. We need to know a good way to choose sigma points
2. We need to know how to predict the sigma points (Insert them into the process function)
3. We need to know how to calculate the prediction, mean, and covariance from the predicted sigma points
