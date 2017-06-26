# Constant Turn Rate & Velocity Magnitude Model (CTRV)

The model we used so far assumes objects are always going straight. The model we will use from now on assumes that objects can move straight, but can also move with a constant turn rate and a constant velocity magnitude.

This model is called the **Constant Turn Rate & Velocity Magnitude Model**

The state vector we will use the two-dimensional position of the bike **px** and **py**, where "p" stands for position. Instead of describing the velocity with vw and vy, we use the *speed and *yaw angle*.

The *speed* is the magnitude of the velocity, which we will call **v**, and the *yaw angle* is the orientation which we will call **psi**

Since we also want to be able to estimate the **yaw rate psi dot product**, we add it to the state vector too. Constant yaw rate and constant speed is a good model for vehicle behavior in real traffic scenarios.

State vector:

```
x = [px     ]
    [py     ]
    [v      ]
    [yaw    ]
    [yaw dot]
```

or

```
x = [px, py, v, yaw, yaw dot]
```

***

### Quiz

In the following quizzes, you'll be using state vectors to draw qualitative observations about the motion of turning objects

State 1:

```
x = [2 m, 4 m, 7 m/s, 0.5 rad, 0.6 rad/s]
```

State 2:

```
x = [2 m, 4 m, 7 m/s, 0.5 rad, 0 rad/s]
```

State 3:

```
x = [2 m, 4 m, 9 m/s, 0.5 rad, 0.6 rad/s]
```

#### Which of the above state vectors represent a car driving on a straight path?

Only the second state vector has a yaw rate of 0

#### Which of the above state vectors has the smallest turning radius?

Though 1 and 3 have the same yaw rate, state vector 1 has a slower speed, meaning the car would make a complete circle in less distance
