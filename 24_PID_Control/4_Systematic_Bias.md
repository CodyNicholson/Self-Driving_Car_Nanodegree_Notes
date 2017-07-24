# Systematic Bias

There is a problem in robotics called "systematic bias". When you ordered your car, you believed the front wheels were 100% aligned, but your mechanic made a mistake and he aligned the wheels a little bit at an angle. For people, that isn't a big concern. When we notice this we just steer a little bit stronger, but how will our proportional controller react? We will set the steering drift to be 10 degrees, which in radians is 10.0/180.0*pi, using the **set_steering_drift()** method.

#### What happens when you run my proportional controller with parameter 0.2, and the differential controller set to 0?

It causes a big cross track error. Put differently, the robot oscillates with a fairly constant new offset error due to this bias. Even if the bias was steering, it manifests itself as an increased cross track error in the **y** direction.

#### Can the differential term solve this problem?

No. The **y** error is still large. is will still converge, but it is still large.
