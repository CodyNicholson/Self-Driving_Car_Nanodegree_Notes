# Parameters & Consistency

This portion is all about how to chose noise parameters and how to evaluate this choice. This is not only related to UKFs, it can also be applied to any Bayesian filter. 

When we talk about our process and our measurement models we introduce several sources of uncertainty. In the process model we introduced the process noise **v_k**

In the measurement model we introduced the measurement noise **w_k**. In the case of a radar measurement, this was the noise of the distance measurement **rho**, the angle measurement **phi**, and the radial velocity **rho dot**.

We also quantified the noise with the process noise covariance matrix and the measurement noise covariance matrix. So these are the variances of the noise and they quantify how strong the noise is.

![alt tag](imgs/noiseUncertainty.png)

LEts start with the measurement noise. This noise describes how precise the sensor can measure. It means we have to look into the sensor manual and see how precise the sensor is. For example, we might read that radar can measure the distance **rho** with the standard deviation of 0.3 meters. This means we know the value for the variance sigma **rho^2**, which is 0.09 m^2. We also have to assume the noise is white and normally distributed, which is of course not true for some sensors. It is a little more difficult to choose an appropriate process noise. In reality, objects in a traffic environment don't move with white acceleration noise. This would mean a driver constantly switches between gas and brake. S we really apply a strong approximation here, by assuming a white process noise. A rule of thumb for getting useful values is the following: Try to estimate what the maximum acceleration is that you expect in your environment. Let's say we want to track cars in an urban environment. Then these cars usually don't accelerate or brake stronger than 6 meters per second^2. The rule of thumb says to choose half of the maximum acceleration you expect as process noise. If this is a good value really depends on your application. If it is important for your application to react fast on changes, then you can choose a process noise that is a bit higher. Is it important to provide smooth estimations? Then you choose the process noise a little lower.

To check if you set up the noise parameters correctly, so you can run a consistency check on the filter. Consistency means that at every time cycle we calculate the measurement prediction **z_(k+1)** and the covariance matrix **s** of this prediction. Then we receive the actual measurement **z_(k+1)** for that time step. Your **z_(k+1)** point should appear inside the ellipse of your uncertainty, meaning your filter is consistent. Sometimes this reading can be wrong, and you might be fine, but if you get a lot of points outside the ellipse then it might be time to reconsider your system. The estimate is less precise than you think if your points are outside the ellipse. Your filter can also be inconsistent if your **z(k+1)** points appear at the very center of the ellipse because then you are overestimating the uncertainty of your system. 

#### A filter is consistent if it provides a realistic estimation of uncertainty

It is very easy to check the consistency of your filter, and you always whould when designing a filter

![alt tag](imgs/nis.png)

An important consistency check is called **nis**, as seen above. The innovation is the difference between the predicted measurement and the actual measurement and normalized means you put it into relation to the covariance matrix **s**. That is why you have the inverse of the matrix **s** in the equation. The **nis** is just a scaler number and super easy to calculate, but you need to know what number to expect. For that you need to know something about the statistics of this nis. The nis value follows a distribution which is called **chi-squared distribution**. This table tells you the number you should expect for your nis. In this table, the **df** column tells you the dimension of our measurement space. In this case we have a three dimensional radar measurement, so we have three degrees of freedom. The **0.95** column says that statistically - in 95% of all cases - you nis will be higher than the number displayed in the cell for whichever dimension you are looking at. The other columns describe other values that your nis will be higher than at a certain percent of the time. You can easily plot this relationship. 
