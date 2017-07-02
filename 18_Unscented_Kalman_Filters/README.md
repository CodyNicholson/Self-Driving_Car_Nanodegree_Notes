# Unscented Kalman Filters

In this unit we learned how UKFs can be used to achieve better results than a EKF. We were first introduced to a more sophisticated process model that is able to estimate the turn rate of a vehicle. Then we were shown how the UKF deals with this nonlinear process model. Lastly, we implemented the filter in C++ and used it to solve a challenging tracking scenario.

## UKF Roadmap

### Prediction

1. Generate sigma points
2. Predict sigma points
3. Predict mean & covariance

### Update

1. Predict measurement
2. Update state
