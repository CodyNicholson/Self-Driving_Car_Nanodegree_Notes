# CTRV Zero Yaw Rate

We now have the solution of the integral. It is a function that brings the state from time step **k** to time step **k+1**. There is only one problem: the division by 0 when the **yaw rate** is 0.

This is an important case because this means that the vehicle is driving straight, which is very common

There are two ways to derive the solution for this special case. You can put the **yaw rate** to 0 right from the beginning and solve the integral again for this case, but you can also directly see the solution in the triangle that is formed by the angle that the car is turning at.

#### How should we calculate the change in the x-position over time when **ψ_k = 0**?

v_k * cos(ψ_k) * t_delta

#### How should we calculate the change in the y-position over time when **ψ_k = 0**?

v_k * sin(ψ_k) * t_delta
