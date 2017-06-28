# CTRV Process Noise Vector

So far we have gone over the deterministic part of the process model, but we also need to consider the stochastic part of the process model, which has a lot to do with the process noise **V_k**.

We will describe the uncertainty of the process model with a two-dimensional noise vector **V_k** consisting of two independent scalar noise processes. The first noise process is the longitudinal acceleration noise: **V_a_k**. It influences the longitudinal speed of the vehicle and it randomly changes its value at every time step **k**.

The longitudinal acceleration is a **normally distributed white noise** with **zero mean** and the variance **sigma_a^2**:

```
V_a_k ~ N(0,sigma_a^2)
```

***

The other noise process is the yaw acceleration **V_psi_dot_dot**. It is also a **normally distributed white noise** with **zero mean** and it has the variance **sigma_psi_dot_dot^2**.

### How does the noise vector V_k influence the process model?

Assuming the yaw acceleration **V_psi_dot_dot** is constant between **k** and **k+1**, it will just linearly add up to the **yaw rate** with increasing time. So the influence of the yaw acceleration on the **yaw rate** is the yaw acceleration times **delta t**.

***

### Quiz

#### What is the influence of v_a_k and v_ψ_k on the velocity?

In other words, what is c in the process model?

**delta t** * **v_a_k**

The acceleration's noise impacts the velocity

#### What is the influence of v_a_k and v_ψ_k on the yaw angle?

**1/2(delta_t)^2 * v_ψ_k**

#### What is the influence of v_a_k and v_ψ_k on the yaw rate?

In other words, what is e in the process model?

**delta_t * v_ψ_k**
