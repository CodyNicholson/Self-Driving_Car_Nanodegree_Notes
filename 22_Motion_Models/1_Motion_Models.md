# Motion Models

The bicycle model is a simple and useful way to represent how a car moves. Like all models, it is based on several simplifying assumptions

First, we ignore all vertical dynamics of the car, so you can assume the car only moves in 2D. Next, we will assume that - like a bicycle - the front wheels of the car are connected to the back wheels of the car by a rigid beam with fixed length. Here we assume that the front two wheels act together so tey can effectively be represented as one wheel - just like a bicycle. The same is true for the two back wheels of the car. Finally, we assume the car is also controlled - like a bicycle - with a steering angle **theta** and some longitudinal velocity in the direction that the car is heading. For this car, we change the steering angle by (pi/8 radians) and then the car moves forward at a velocity of 3 meters per second.

The motion of a car can be simplified to that of a bike using the above assumptions, so we can model the two very similarly
