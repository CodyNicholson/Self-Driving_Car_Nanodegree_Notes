# Limit Distribution

Suppose we have five grid cells in a one-dimensional cyclical world again with an initial distribution that assigns 1 to the first grid cell and 0 to all the others: 1, 0, 0, 0, 0

Let's assume **U** is 1 which means that there is a 0.8 chance that the car will move to cell two, 0.1 chance that we will not move at all, and 0.1 chance we will move to cell three during the next motion step.

Lets say we have an unlimited amount of motion steps - what happens to the probability distribution? As you might expect, it will gradually become a uniform distribution of: 0.2, 0.2, 0.2, 0.2, 0.2. This is because as the car keeps moving over and over we lose more and more certainty about where the car will be until we finally reach maximum uncertainty - the uniform distribution.

##### Every time we move we lose information
