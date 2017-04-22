#Perceptron Training

Given examples, find weights that map inputs to outputs

To do this we use two different rules that have been developed to do this:

- Perceptron Rule (With Threshold)
- Gradient Decent/Delta Rule (Without Threshold)

***

###Perceptron Rule

This rule tells us how to set the weights of a single unit so that it matches some training set

Our training set is a bunch of examples of x (inputs) represented in vectors and a vector of y's that are the outputs that we want to hit. 

We need to give a learning rate for the weights W and not give a learning rate for the theta, but we do need to know the theta.

Out goal is to set the weights so that our inputs will produce the correct outputs as much as possible.

If the output is already correct either both on or both off, then no change to the weights. However, if the output is wrong then we need to make 

The Learning Rate says that we will figure out the direction that we want to move things and just take a little step in that direction. 

***

###Gradient Descent

When we are given a problem that cannot be solved using a linear function, we should use Gradient Descent instead of the Perceptron Rule

In Gradient Descent we imagine the output is not thresholded

a = Summation(xi*wi)

***

###Comparison Of Learning Rules

Perceptron Rule that guarantees of finite convergence: Change in Wi = N(y-y^) * Xi

Gradient Descent that is more robust to datasets that are not linearly separable, but will only converge in a limit to a local optimum: Change in Wi = N(y - a) * Xi
