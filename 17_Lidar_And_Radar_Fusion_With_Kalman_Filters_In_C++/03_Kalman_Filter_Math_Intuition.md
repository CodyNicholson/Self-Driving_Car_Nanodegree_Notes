# Kalman Filter Math Intuition

X = A single pedestrian we are tracking using a Kalman Filter with a position value: *p*, and a velocity value: *v*

### State Transition Function

x_i = f(x) + v

v ~ N(0, Q)

### Measurement Function

z = h(x_i) + w

w ~ N(0,R)

***

The first terms of the above functions: f(x) and h(x_i) represent the deterministic part of the model

The last terms: nu noise (*v*) and omega noise (*w*), represent the stochastic part. In other words, random noises that affect the prediction and measurement update steps.

***

### Linear Motion Model

p_i = p + v(delta_t)

v_i = v

By using the linear motion model with a constant velocity, the new location of our pedestrian *p* is the old position + *v* multiplied by delta *t*

Since velocity is constant, the new velocity is the same as the old velocity. We can express this in matrix form like this:

```
(p_i) = (1, delta(t)) (p)
(v_i) = (0, 1       ) (v)
```

***

For the measurement function, our vehicle only senses the pedestrian position, so the measurement function looks like this:

z + p_i

In matrix format:

```
z = (1, 0) (p_i)
		   (v_i)
```

 ***

The Kalman Filter algorithm is composed of a prediction step where we predict our state and covariance *p*:

```
x_i = F_x + v
P_i = FPF_T + Q
```

We also use a measurement update step, often called the correction step where we use the latest measurement to update the state estimate and its uncertainty

```
y = z - Hx_i

S = (H)(P_i)(H_T) + R

K = (P_i)(H_T)(S^-1)

x = x_i + K_y

P = (I - KH)(P_i)
```

***

### Kalman Filter Intuition

The Kalman equation contains many variables, so here is a high level overview to get some intuition about what the Kalman filter is doing.

#### Prediction

Let's say we know an object's current position and velocity , which we keep in the x variable. Now one second has passed. We can predict where the object will be one second later because we knew the object position and velocity one second ago; we'll just assume the object kept going at the same velocity.

The *x_i = Fx + ν* equation does these prediction calculations for us

But maybe the object didn't maintain the exact same velocity. Maybe the object changed direction, accelerated or decelerated. So when we predict the position one second later, our uncertainty increases. *P_i = FPF_T + Q* represents this increase in uncertainty.

Process noise refers to the uncertainty in the prediction step. We assume the object travels at a constant velocity, but in reality, the object might accelerate or decelerate. The notation *v ~ N(0,Q)* defines the process noise as a Gaussian distribution with mean zero and covariance Q.

#### Update

Now we get some sensor information that tells where the object is relative to the car. First we compare where we think we are with what the sensor data tells us *y = z−Hx_i*

The *K* matrix, often called the Kalman filter gain, combines the uncertainty of where we think we are *P_i* with the uncertainty of our sensor measurement *R*. If our sensor measurements are very uncertain (R is high relative to P'), then the Kalman filter will give more weight to where we think we are: *x_i*. If where we think we are is uncertain (P' is high relative to R), the Kalman filter will put more weight on the sensor measurement: *z*.

Measurement noise refers to uncertainty in sensor measurements. The notation *ω∼N(0,R)* defines the measurement noise as a Gaussian distribution with mean zero and covariance R. Measurement noise comes from uncertainty in sensor measurements.


### A Note About the State Transition Function: Bu

If you go back to the video, you'll notice that the state transition function was first given as *x_i = Fx+Bu+ν*

But then Bu was crossed out leaving *x = Fx+ν*

*B* is a matrix called the control input matrix and u is the control vector

As an example, let's say we were tracking a car and we knew for certain how much the car's motor was going to accelerate or decelerate over time; in other words, we had an equation to model the exact amount of acceleration at any given moment. *Bu* would represent the updated position of the car due to the internal force of the motor. We would use *ν* to represent any random noise that we could not precisely predict like if the car slipped on the road or a strong wind moved the car.

For the Kalman filter lessons, we will assume that there is no way to measure or know the exact acceleration of a tracked object. For example, if we were in an autonomous vehicle tracking a bicycle, pedestrian or another car, we would not be able to model the internal forces of the other object; hence, we do not know for certain what the other object's acceleration is. Instead, we will set *Bu=0* and represent acceleration as a random noise with mean *v*.
