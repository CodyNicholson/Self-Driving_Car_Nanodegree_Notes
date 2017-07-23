# Comparing Filters

The **histogram filter** is discrete (The distribution was defined over a finite set of bins) and is multi-model (described multiple bumps) and scales exponentially (Any grid defined over **k** dimensions will have exponentially many grid cells in the number of dimensions) and are approximate

The **Kalman filter** has a continuous state space and is uni-model (could only describe one bump at a time (Single Gaussian)) and is quadratic (All we represented was a vector, the mean, and the covariance matrix) and are approximate

The **particle filter** has a continuous state space and is multi-model and scales exponentially in some cases but in the case of tracking domains scales much better and is easy to program
