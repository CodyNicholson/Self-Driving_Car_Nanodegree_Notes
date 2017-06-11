# Variance Comparison

Wide Gaussian distributions have large covariance

In the formula: f(x) = 1/square(2*Pi*Variance^2) exp(-1/2((X - Mu)^2/Variance^2))

The difference between X and Y is being normalized by the covariance. The larger the value of (X - Mu), the less difference in the variance (width) matters, and as a result, the more the function is spread out.

Put differently, the variance^2 covariance is a measure of uncertainty. The larger variance^2, the more uncertain we are about the actual state. The narrow distributions with small deviations are very certain, while wider distributions with large deviations are less certain.

*In our self-driving car algorithms, we will always prefer a narrow Gaussian because we always want to be very certain of what we are doing*
