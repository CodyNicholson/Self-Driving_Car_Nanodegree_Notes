# Radar Measurement

So far we have implemented a Kalman Filter that uses a Lidar, but now we will integrate a Radar sensor as well to improve our accuracy. Although the lidar provides pedestrian positions with high accuracy, we don't have a way to observe the pedestrian's speed. That is where radars can help us

Using the **Doppler effect**, the radar can directly measure the radial velocity of a moving object. The **Radial Velocity** is the component of velocity moving towards or away from the sensor. However, the Radar has a *lower spacial resolution than the laser sensors*, all the more reason we should combine both of these sensors.

We will redesign our Kalman Filter to work with new radar information. The **state transition function** will be exactly what we designed in the lidar case. We use the same state with four parameters: **Px, Py, Vx, Vy**, with the same linear motion model and process noise. However, our new radar sees the world differently. The x-axis always points in the vehicle's direction of movement and the y-axis points to the left. Instead of 2D position, the radar can directly measure the object range: **rho**, bearing:  **phi**, and radial velocity/range rate: **rho dot**. 

#### The Range: rho

is the radial distance from the origin to our pedestrian. So we can always define a ray which extends from the origin to our object position.

#### The Bearing: phi

is the angle between the ray and x-direction

#### The range rate (radial velocity): rho dot

is the velocity along this ray

***

Similar to our motion model, the radar observations are corrupted by a zero-mean random noise omega. Since the three measurement vector components are not cross-correlated, their radar measurement covariance matrix becomes a 3-by-3 diagonal matrix.

So, our state is still the same and has four parameters: **Px, Py, Vx, Vy**, and the measurement vector has three parameters: **rho, phi, rho dot**

***

#### What is the measurement function h of x prime that maps the predicted state x prime into the measurement space?

The h function specifies how the predictive position and speed can be related to the object range, bearing, and range rate
