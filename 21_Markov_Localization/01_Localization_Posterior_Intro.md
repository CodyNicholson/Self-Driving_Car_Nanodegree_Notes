# Localization Posterior Intro

Given a map with landmarks in a global coordinate system, observations from the onboard sensor in the local coordinate system, and the information how the car moves between two time steps. Formally, the observations are defined as a vector **z** which includes all observations from time step 1 to **t**. The observations could be range measurements, bearing angles, or images. We also have the controls of the car as a vector **u**, which includes all control elements from time step 1 to **t**. Typically we will have **yaw**, **pitch**, or **roll rates**, and **velocity information**. Last, we have the map which could be a grid map of the global environment or a database which includes global feature points and the lane geometry. Here we do not add the time index **t** to the map because we assume that the map does not change over time, and we assume these variables are known.

What we want to estimate is the transformation between the local coordinate system of the car and the global coordinate system of the map. If we know this transformation, then we also know the pose of the car in the global map.

The position fo the car at time **t** is defined with **x**. If we assume we have a 2D map, for example: **x** includes a position with **x** and **y** coordinates, and also the orientation **phi**. The values of the state **x_t** will never be perfectly accurate. What we want it to form a sufficiently accurate belief of the state **x_t**. We want to formulate this belief in a probabilistic way. 

#### The belief of x_t is the posterior distribution of x_t given all observations, the controls and the map
