# Motion Models

In this section we reviewed vehicle movement and motion models so we can predict where a self-driving car will be at some future time. Predicting motion is a big step for making a mobile robot drive itself.

Motion models are an important part of many localization algorithms. For example, in Bayesian methods, motion models are used in the predictive step.

In order to predict the location of a car we need to know about how cars move, so we will use some physics to create our bicycle motion model to estimate the position of the car given sensor data such as the number of wheel turns, velocity, and/or the yaw rate.

We learn:

- The bicycle motion model
- How to calculate new positions given **yaw rate**, **velocity**, and **odometry**
- Limitations of odometry

