# CTRV Process Noise Position

Now we will look at the influence of the noise vector on the position. We assume that the effect of the yaw acceleration on the position is relatively small in comparison to other factors.

This time instead of a constant velocity we need to assume a constant acceleration and then solve the integral for that case. We can approximate this by using the acceleration offset of a car driving exactly straight.

#### What would the x acceleration offset be if the car were driving perfectly straight? In other words, what is a?

```
1/2(delta_t)^2 * cos(ψ_k) * v_a_k
```

#### What would the y acceleration offset be if the car were driving perfectly straight? In other words, what is b?

```
1/2(delta_t)^2 * sin(ψ_k) * v_a_k
```
