#Minimizing Cross Entropy

#####D(S(w*x+b),L)

#####D(A,a) D(A,b)

How are we going to find those weights (w) and those biases (b)) that will get our classifier to do what we want it to do - That is, have a low distance for the correct class but have a high distance for the incorrect class

One of the methods for doing this is to measure the distance averaged over the entire training sets for all inputs and all labels that you have available. This is called the **Training Loss** and it is calculated like this:

Training Loss = 1/N * (Summation i(D(S(w*x_i + b), L_i)))

The Training Loss is the average cross-entropy over your entire training set in one big function seen above. Every example in your training set gets multiplied by one big matrix W (weights), and then summed together in one big summation. Ideally, we want all the distances to be small - meaning that we are doing a good job at classifying every example in the training data. Loss should be small. The Loss is a function of the weights and the biases, so we will simply try and minimize that function.

If the loss is a function of two weights that are large in some areas and small in others. We're going to try the weights which cause this loss to be the smallest, which means we have turned the machine learning problem into one of numerical optimization. This is good because there are lots of ways to solve a numerical optimization problem, the simplest of which is Gradient Descent. This means we will take the derivative of our loss with respect to your parameters and follow that derivative by taking a step backwards and then repeat until you get to the bottom.
