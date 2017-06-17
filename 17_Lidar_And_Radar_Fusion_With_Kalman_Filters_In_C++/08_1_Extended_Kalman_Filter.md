# Extended Kalman Filter

If we have our predicted state **x** described by a Gaussian distribution, if we map this Gaussian to a nonlinear function **h**, then the result *is not a Gaussian distribution anymore*. Thus, the Kalman Filter is no longer applicable.

To fix this, we can linearize the **h(x)** function. This is the key idea behind the extended Kalman Filter.

We have to approximate our measurement function **h** by a linear function which is tangent to **h** at the mean location of the original Gaussian. We pass all the **x_i** values through the linear approximation of **h**. The resulting distribution will now maintain the Gaussian-like shape.

#### How do we linearize a Gaussian function?

The extended Kalman filter uses a method called **first order Taylor expansion**

We first evaluate the nonlinear function **h** at the mean location **mu**, which is the best estimate of our predicted distribution. Then, we extrapolate the line with slope around **mu**. This slope is given by the first derivative of **h**.
