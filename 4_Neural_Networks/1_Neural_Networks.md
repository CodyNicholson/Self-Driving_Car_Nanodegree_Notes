#Neural Networks

A neural network in AI is designed to mimic the brain. Our AI neural network has neurons that fire under different conditions. We train these neurons so that they know when to fire.

***

###Perceptron

A Perceptron is a specific kind of neuron in a neural network.

A Perceptron has inputs that we will denote as x1, x2, ..., xi and each input has a corresponding weight that we denote as w1, w2, ..., wi

The weighs are there to turn up the gain, or the sensitivity of the neuron since we will multiply all the inputs by their corresponding weights. 

Since different inputs (x) have different weights (w), and each input is multiplied by its corresponding weight, we can use the weight to determine how sensitive our neuron will be to certain inputs.

We take the sum of all the products that we get from multiplying each input by its corresponding weight. Then we see if this sum, called the **activation**, is greater than the **firing threshold**. If it is we return 1, and if it isn't we return 0.

***

#Artificial Neural Networks Example

x1 = 1, w1 = 1/2

x2 = 0, w2 = 3/5

x3 = -1.5, w3 = 1

Firing Threshold = 0

activation = (x1*w1) + (x2*w2) + (x3*w3) = 0.5 + 0 + -1.5 = -1

activation = -1, since -1 is not greater than or equal to the firing threshold, y=0 (The neuron does not activate)
