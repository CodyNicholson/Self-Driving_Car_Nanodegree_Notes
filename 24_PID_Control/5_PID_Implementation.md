# PID Implementation

If you drive a car and your normal steering mode leads you to a trajectory far away from the goal, then what I submit you do is you notice over a long period of time you can't get closer. So you start steering more and more the more time goes by to the right to compensate this bias. You adjust to the bias. As a result, when you drive you steer the car a bit more. To do so we need a sustained situation of large error. That's measured by the integral, or the sum of the cross track errors over time. Let's make a new controller where steering is proportional to the cross track errors before is is equally proportional to the differential of the cross track error, but now it is also proportional to what's called the integral of the sum of all the cross track errors you ever observed. If we have a constant cross track error of 0.8, and the sume will increase by 0.8 for each time unit, it'll become larger and eventually it'll correct the robot's motion. This is called a **PID Controller**. 

![alt tag](imgs/pidControllerFormula,PNG)

The integrated cross track error is the sum of all cross track errors you have ever observed

### Code

```python
# Implement a P controller by running 100 iterations
# of robot motion. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
#
# where the integrated crosstrack error (int_CTE) is
# the sum of all the previous crosstrack errors.
# This term works to cancel out steering drift.

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

def run(robot, tau_p, tau_d, tau_i, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    prev_cte = robot.y
    int_cte = 0
    for i in range(n):
        cte = robot.y
        diff_cte = cte - prev_cte
        prev_cte = cte
        int_cte += cte
        steer = -tau_p * cte - tau_d * diff_cte - tau_i * int_cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
    return x_trajectory, y_trajectory

robot = Robot()
robot.set(0, 1, 0)

def run(robot, tau_p, tau_d, tau_i, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    # TODO: your code here
    run(robot, tau_p, tau_d, tau_i)
    return x_trajectory, y_trajectory

x_trajectory, y_trajectory = run(robot, 0.2, 3.0, 0.004)
n = len(x_trajectory)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))
ax1.plot(x_trajectory, y_trajectory, 'g', label='PID controller')
ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')
```

Ok. With the integral term we're keeping track of all the previous CTEs, initially we set int_cte to 0 and then add the current cte term to the count int_cte += cte. Finally we update the steering value, -tau_p * cte - tau_d * diff_cte - tau_i * int_cte with the new tau_i parameter.

```python
def run(robot, tau_p, tau_d, tau_i, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    prev_cte = robot.y
    int_cte = 0
    for i in range(n):
        cte = robot.y
        diff_cte = cte - prev_cte
        prev_cte = cte
        int_cte += cte
        steer = -tau_p * cte - tau_d * diff_cte - tau_i * int_cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
    return x_trajectory, y_trajectory
```

![alt tag](imgs/pid.png)

```python
int_cross_track_error = 0.0

cross_track_error = myrobot.y

for i in range(N):
	diff_cross_track_error = myrobot.y - cross_track_error
	cross_track_error = myrobot.y
	int_cross_track_error += cross_track_error
	steer = - param1 * cross_track_error \ - param2 * diff_cross_track_error \ - param3 * int_cross_track_error
	myrobot = myrobot.move(steer, speed)
	print myrobot, steer
```
