#How Powerful Is The Perceptron Unit?

A Perceptron Unit returns either 0 or 1 based on the inputs and weights

We can express And, Or, and Not using Perceptron Units in a machine learning algorithm

***

###And

w1 = 1
w2 = 1
theta = 2

The above values will simulate a "And" case using Perceptrons. This is because if our inputs are 1 and 0 then (1*1 + 0*1) will give us 1 which is less than 2. However, if we have both our inputs as 1 then we get 2 which is greater than or equal to 2, thus only both of them being one will be enough to activate this neuron.

-

###Or

If we have two inputs x1 and x2 and we want to make and Or case can make w1 and w2 and theta (threshold) equal to 1. That way, if our inputs are both 0 then (0*1 + 0*1) will give us 0 - a value below the threshold. If we input x1 as 1 and x2 as 0 then (1*1 + 0*1) will give us 1 which is greater than or equal to our threshold 0. If both inputs are 1 we get 2 that is greater than or equal to our threshold. This is how we simulate "Or" with Perceptrons.

-

###Not

If we make w1 = -1 and theta (threshold) = 0, then for all inputs (x) that are greater than 0, they will be multiplied by the weight of -1 and will thus be below the threshold of 0. For all inputs (x) less than 0, they will be multiplied by -1 and thus become positive, making them larger than the threshold of 0. This is how we simulate a "Not" case with Perceptrons.
