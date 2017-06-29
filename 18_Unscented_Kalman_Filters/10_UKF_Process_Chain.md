# UKF Process Chain

Now that we have learned the CTRV motion model equations, we will discuss how the unscented Kalman filter works. Recall that the extended Kalman filter uses the Jacobian matrix to linearize non-linear functions.

The unscented Kalman filter, on the other hand, does not need to linearize non-linear functions; instead, the unscented Kalman filter takes representative points from a Gaussian distribution. These points will be plugged into the non-linear equations as you'll see in the lectures.

***

What we have derived from the CTRV model is a process model that considers the possibility to drive on a straight line, or doing a turn. This is good because it helps us to achieve good results when tracking a bike.

The way the unscented Kalman filter processes measurements over time is exactly the same as the extended Kalman filter:

We have a prediction step, which is independent of the measurement model. In this step, you will use the CTRV model we just delivered.

Then we have an update step where we use the radar measurement model, or the laser measurement model depending on the type of measurement we just received. This means you'll be able to apply the same top level processing chain for the unscented Kalman filter as you use for the extended Kalman filter.

The difference between the unscented and extended Kalman filters is how the unscented Kalman filter deals with nonlinear process models or measurement models. For these cases, the UKF uses an approach called unscented transformation.
