# Gaussian Intro

In Kalman Filters the distribution is given by what's called a Gaussian

*Gaussian* is a continuous function over the space of locations where the area underneath sums up to one

A Gaussian is characterized by two parameters: a mean (mu), and the width of the Gaussian (variance). A 1-D Gaussian is characterized by:

> (Mu * Variance^2)

Our task in Kalman Filters is to maintain a mu and variance^2 that is the best location of the object we are trying to find. The exact formula is an exponential of a quadratic function where we take the exponential of:

If X equals Mu, then the enumerator becomes 0 and we have X of 0 which is 1. We have to normalize this by a constant:

> f(x) = 1/square(2*Pi*Variance^2) exp(-1/2((X - Mu)^2/Variance^2))

A Gaussian is just a single hill on a graph, which is why it is called uni-modal since it only has one hill

##### Note

The "exp" stands for "exponential". The term "exp(x)" is the same as writing ex or e^x or "e to the x" or "e to the power of x". In this context, "e" is a universal constant, e = 2.718281828...
