# Intro To Unscented Kalman Filters

Another technique for cruise control in a car with automatic distance keeping you will find an Extended Kalman Filter, but there is also another technique called an **Unscented Kalman Filter (UKF)** that can achieve even better results.

The UKF is an alternative technique to deal with norming your process models, or non-linear measurement models. Instead of linearizing a nonlinear function, the UKF uses **sigma points** to approximate the probability distribution.

This has two advantages:

- In many cases the sigma points approximate the nonlinear transition better than a linearization does
- It is not necessary to calculate a Jacobian matrix

