# Limitations Of The Constant Velocity Model

Since we used a constant velocity model thus far in our Kalman Filter implementations, we have been simplifying the problem. In the real-world there is acceleration and deceleration, particularly when the car turns.

Our current Kalman Filter implementations don't account for changes in velocity and direction, and will predict the position of a turning vehicle incorrectly.

***

Assume a vehicle drives straight at first and then goes into a turn. If we apply a Kalman Filter to track the vehicle (using the process model from the last lesson, which assumes constant velocity), what do you expect to happen with our estimation result for the vehicle position?

The process model would assume the car is moving tangentially to the circle, resulting in a predicted position outside of it.
