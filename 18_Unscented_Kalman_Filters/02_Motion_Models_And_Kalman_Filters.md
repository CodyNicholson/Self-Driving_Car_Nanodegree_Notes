# Motion Models & Kalman Filters

In the extended Kalman filter lesson, we used a *constant velocity* model (CV). A constant velocity model is one of the most basic motion models used with object tracking.

But there are many other models including:

- constant turn rate and velocity magnitude model (CTRV)
- constant turn rate and acceleration (CTRA)
- constant steering angle and velocity (CSAV)
- constant curvature and acceleration (CCA)

Each model makes different assumptions about an object's motion. In this lesson, you will work with the CTRV model.

Keep in mind that you can use any of these motion models with either the extended Kalman filter or the unscented Kalman filter, but we wanted to expose you to more than one motion model.
