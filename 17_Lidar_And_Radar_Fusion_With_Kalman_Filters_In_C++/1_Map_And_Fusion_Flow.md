# Map & Fusion Flow

First, we will build an extended Kalman filter, It is extended in the sense that it will be capable of handling more complex motion models and measurement models. The overall processing flow, as seen in the picture below, has two sensors: a lidar and a radar. The information provided by these sensors is used to estimate the state of a moving pedestrian and the state is represented by a 2D position and a 2D velocity.

Each time we receive new measurements from a given sensor the estimation function is triggered which you can find in the picture by following the "First Measurement" node down the "no" branch. 

In the estimation function we perform two steps, state prediction and measurement update. In the prediction step we predict the pedestrian state and its covariance. We do so by taking into account the elapsed time between the current and previous operations. The measurement update step depends on the sensor type.

If the sensor is a laser sensor, then we just apply a standard Kalman filter to update the pedestrian's state

The radar measurement involves a nonlinear measurement function, so when we receive our radar measurements we use different tweaks to handle the measurement update. For example, we may use the extended Kalman Filter equations.

![alt tag](imgs/KalmanFilterAlgMap.png)

For your reference: a map of the Kalman Filter algorithm! Keep an eye out, because we'll add a little bit more detail to this later.

Imagine you are in a car equipped with sensors on the outside. The car sensors can detect objects moving around: for example, the sensors might detect a bicycle.

The Kalman Filter algorithm will go through the following steps:

- *first measurement* - the filter will receive initial measurements of the bicycle's position relative to the car. These measurements will come from a radar or lidar sensor.
- *initialize* state and covariance matrices - the filter will initialize the bicycle's position based on the first measurement.
- then the car will receive another sensor measurement after a time period Δt.
- *predict* - the algorithm will predict where the bicycle will be after time Δt. One basic way to predict the bicycle location after Δt is to assume the bicycle's velocity is constant; thus the bicycle will have moved velocity * Δt. In the extended Kalman filter lesson, we will assume the velocity is constant; in the unscented Kalman filter lesson, we will introduce a more complex motion model.
- *update* - the filter compares the "predicted" location with what the sensor measurement says. The predicted location and the measured location are combined to give an updated location. The Kalman filter will put more weight on either the predicted location or the measured location depending on the uncertainty of each value.
- then the car will receive another sensor measurement after a time period Δt. The algorithm then does another predict and update step.
