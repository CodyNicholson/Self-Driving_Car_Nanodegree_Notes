# Extended Kalman Filter Algorithm Generalization

How do we put our original Kalman Filter and the Extended Kalman Filter together?

We start by changing the original Kalman Filter by adding the non-linear function **f(x)** to predict the state, and **h(x)** to compute the measurement error here. Additionally, the state transition matrix **F** and the measurement matrix **H** are replaced by corresponding Jacobians: **Fj** and **Hj**.

First we have to compute these Jacobian matrices. Since the linearization points change, we have to recompute the Jacobians at every point in time. For the Extended Kalman Filter, we linearize the nonlinear prediction measurement functions, and then we use the same mechanism to estimate the new state.
