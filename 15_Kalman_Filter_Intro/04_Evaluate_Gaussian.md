# Evaluate Gaussian

```python
from math import *

def f(mu, sigma2, x):  # mu is mean, sigma2 is variance^2
	return 1/sqrt(2.*pi*sigma2) * exp(-.5 (x-mu)**2 / sigma2)

print f(10., 4., 8.)
# prints 0.12098536226
```

### Maximize Gaussian

By setting x to the same value as mu (the mean), we get the peak of the Gaussian

```python
#For this problem, you aren't writing any code.
#Instead, please just change the last argument 
#in f() to maximize the output.

from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print f(10.,4.,10.) #Change the 8. to something else!
# prints 0.199471140201
```
