# Oscillations

Oscillate - move or swing back and forth at a regular speed, vary in magnitude or position in a regular manner around a central point

```python
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
    
x_trajectory, y_trajectory = run(robot, 0.1)  <-- tau parameter changes from 0.1 to 0.3
n = len(x_trajectory)
```

Tau, the control parameter, changes from 0.1 to 0.3. What happens?

It will oscillate faster. For the larger value of 0.3, we reach a negative value in **y** already, which means we just crossed the line after 13 steps.
