# CTRV Differential Equation

The goal of the process model **f** is to predict where the car will be at time (**k** + 1), given **k** which is the car's current location and a noise vector **new k**.

#### State Vector:

```
x = [px, py, v, yaw, yaw dot]
```

#### Process Model:

```
x_(k+1) = f(x_k, v_k)
```

#### Change Rate of the State x:

```
x_changeRate = [px_change, py_change, v_change, yaw_change, yaw dot_change]
```

From the geometric relations we can directly derive how the change rate **x dot** depends on the state **x**. This is a differential equation:

#### Differential Equation:

```
x_change = g(x)
```

***

**px dot** is the same as the velocity in **x** direction. However, the velocity in **x** direction is not part of the state vector. The speed **v** and the yawing of **psi** are both elements of the state vector. If we look at the triangle created by the outside angle of a turning car, we can identify that **vx** = **cos(psi)** * **v**.
