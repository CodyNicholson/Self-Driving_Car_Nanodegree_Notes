# Parameter Update

Suppose we multiply two Gaussians as in Bayes rule, a prior and a measurement probability

The Prior has a mean of mu and a variance of sigma^2

The measurement has a mean of nu and a covariance of r^2

The new mean, mu prime, is the weighted sum of the old means where mu is weighted by r^2 and nu is weighted by sigma^2 normalized by the sum or the weighted factors:

mu prime = ((mu * r^2) + (nu * sigma^2))/(r^2 + sigma^2)

sigma^2 prime (variance term) = 1/((1/r^2) + (1/sigma^2))

In the example Gaussian distributions, the prior is wider and thus has higher uncertainty, therefore sigma^2 must be larger. This also means that nu is weighted much larger than the mu.

The variance term is unaffected by the actual means. IT just uses the previous variances and comes up with a new one that is narrower.

***

### Code

```python
# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]

print update(10.,8.,13., 2.)
# prints [12.4, 1.6000000000001]
```
