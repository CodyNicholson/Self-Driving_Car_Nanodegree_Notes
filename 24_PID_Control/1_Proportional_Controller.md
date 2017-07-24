# Proportional Control

Assume we have a car with a steerable front axle and 2 non-steerable back wheels. We want the car to drive along a line, and the car has a fixed forward velocity, but we have the ability to set the steering angle of the car.

The best way to control the car in this case is to *steer proportionate to the __cross track error__*, which is the lateral distance between the vehicle and the so-called reference trajectory. This means the larger the error, the more you're willing to turn towards the target trajectory.

What we just learned is called a "P-Controller" where **P** stands for proportional. Suppose we steer in proportion to the cross track error. That is, your steering angle is proportional by come factor of **tau** to the cross track error. What will happen to the car? It will overshoot its target. The problem is that - no matter how small this **tau** constant is - it will eventually turn its wheels towards its trajectory. Then it will move towards its trajectory more and more. When it hits it, it's wheels will be straight, but the robot itself will still be oriented a little bit downwards, so it is forced to overshoot.

This means that when applied to a car, a P-controller will slightly overshoot (which could be OK if it is only a little bit). The overshooting is very small. It never really converges. It'll be what's called "marginally stable" or often just "stable".

***

### Coding A P-Controller

In the code below, there is a class "robot" that we have used before. It has an "init", a **set()** function, and a **set_noise()**function. There is also a function called **set_steering_drift()** which we won't look at just now. There is also a **move()** method.

Our goal is to implement the **run()** command, which takes as input the control parameter that governs the proportional response of the steering angle to the cross track error. The robot has an initial position of 0, 1, and 0 with a speed of 1, and a simulation consisting of 100 steps **N**.

Our robot is initially off the x-axis by 1. We want the car to drive along the **x**-axis so that the **y**-value is the same as the cross track error. By turning inversely proportional to the **y**-value using a parameter **tau** that sets the response strength of the proportional controller. We want the robot to turn towards the **x**-axis, drive in that direction, overshoot, turn around, drive back. To do this, simulate the world for 800 steps, and use a proportionality term that sets my steering angle **alpha** in proportion to the cross track error **y**. 

```python
# Implement a P controller by running 100 iterations
# of robot motion. The desired trajectory for the 
# robot is the x-axis. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau * crosstrack_error
#
# You'll only need to modify the `run` function at the bottom.
 
import random
import numpy as np
import matplotlib.pyplot as plt

# this is the Robot class
class Robot(object):
    def __init__(self, length=20.0):
        """
        Creates robot and initializes location/orientation to 0, 0, 0.
        """
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    def set(self, x, y, orientation):
        """
        Sets a robot coordinate.
        """
        self.x = x
        self.y = y
        self.orientation = orientation % (2.0 * np.pi)

    def set_noise(self, steering_noise, distance_noise):
        """
        Sets the noise parameters.
        """
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = steering_noise
        self.distance_noise = distance_noise

    def set_steering_drift(self, drift):
        """
        Sets the systematical steering drift parameter
        """
        self.steering_drift = drift

    def move(self, steering, distance, tolerance=0.001, max_steering_angle=np.pi / 4.0):
        """
        steering = front wheel steering angle, limited by max_steering_angle
        distance = total distance driven, most be non-negative
        """
        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = np.tan(steering2) * distance2 / self.length

        if abs(turn) < tolerance:
            # approximate by straight line motion
            self.x += distance2 * np.cos(self.orientation)
            self.y += distance2 * np.sin(self.orientation)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
        else:
            # approximate bicycle model for motion
            radius = distance2 / turn
            cx = self.x - (np.sin(self.orientation) * radius)
            cy = self.y + (np.cos(self.orientation) * radius)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
            self.x = cx + (np.sin(self.orientation) * radius)
            self.y = cy - (np.cos(self.orientation) * radius)

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]' % (self.x, self.y, self.orientation)

robot = Robot()
robot.set(0, 1, 0)

def run(robot, tau, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    for i in range(n):
        cte = robot.y
        steer = -tau * cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
    return x_trajectory, y_trajectory
    
x_trajectory, y_trajectory = run(robot, 0.1)
n = len(x_trajectory)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(x_trajectory, y_trajectory, 'g', label='P controller')
ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')
```

The cross track error, **cte** is the current y position of the robot (our reference is a horizontal line) along the x-axis. To get the steering value we multiply the **tau** parameter with the **cte**. We then call the **move** method which causes the robot to move based on the **steer** and **speed** values. Add the **x** and **y** coordinates to the respective lists and then return them at the end.
