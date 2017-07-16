# Localization Posterior Intro

Given a map with landmarks in a global coordinate system, observations from the onboard sensor in the local coordinate system, and the information how the car moves between two time steps. Formally, the observations are defined as a vector **z** which includes all observations from time step 1 to **t**. The observations could be range measurements, bearing angles, or images. We also have the controls of the car as a vector **u**, which includes all control elements from time step 1 to **t**. Typically we will have **yaw**, **pitch**, or **roll rates**, and **velocity information**. Last, we have the map which could be a grid map of the global environment or a database which includes global feature points and the lane geometry. Here we do not add the time index **t** to the map because we assume that the map does not change over time, and we assume these variables are known.

What we want to estimate is the transformation between the local coordinate system of the car and the global coordinate system of the map. If we know this transformation, then we also know the pose of the car in the global map.

The pose for the car at time **t** is defined with **x**. If we assume we have a 2D map, for example: **x** includes a pose with **x** and **y** coordinates, and also the orientation **phi**. The values of the state **x_t** will never be perfectly accurate. What we want it to form a sufficiently accurate belief of the state **x_t**. We want to formulate this belief in a probabilistic way. 

#### The belief of x_t is the posterior distribution of x_t given all observations, the controls and the map

***

### Localization Posterior Explanation & Implementation

Localization is all about estimating the probability distribution of a state, **x_t**, which is the position of the car, another condition that all previous observations **z** from time 1 to **t** and all previous controls **u** from time 1 to **t** are given. To solve the pure localization problem we assume that the map is correct and does not change. Therefore, the map is also given. If we would like to estimate the map as well, then we would solve the simultaneous localization and mapping problem, called the **SLAM problem**, which is much more complex. Are focus will be the posterior distribution:

```
bel(x_t) = p(x_t|z_1:t, u_1:t, m)
```

#### The Map

The map includes the position of street lamps and trees in 1D. This means we are working with landmark-based maps, which are more sparse than grid-based maps. In the 1D case, the map is a vector of the pose where these objects are. On our example map there is a list of landmarks, **m** (map), with six values: 

```
m = 9, 15, 25, 41, 59, 777
```

For the observation we state that the car measures the nearest **k** seen steady objects in driving direction. So we assume that the car can detect the distances to street lamps and trees. This results in a **observations list** which includes, for each time step **t**, a vector of distances, **z_t**, from 1 to **z_t** to **k**:

```
Observation list:

z_1:t = {z_t, ..., z_1}

Vector of Distances:

z_t = [z_t_1, ..., z_t_k]
```

The control vector includes a direct move of the car between consecutive time steps. This means the control is defined by the distance the car traveled between **t** and **t - 1**. The true pose of the car is somewhere in the mapped area.

```
Control Vector:

u_1:t = [u_t, ..., u_1]
```

Since the map is discrete, the pose of the car could be any integer between 0 and 1990 meters. This means the belief of **x_t** is defined as a vector of 100 elements, and each element represents a probability that the car is located at a corresponding position. The goal is to estimate these values.
