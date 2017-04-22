#Helping SGD With Momentum & Learning Rate Decay

###Basics

####1. Helping with the Inputs:

- Make your inputs mean 0
- Give them equal variance (small)

####2. Helping initial weights

- Initialize with random weights
- Have their mean be equal to 0 as well
- Also give them equal variance (small)

***

###New Tricks

####Momentum

At each step we are taking a very small step in a random direction, but then on aggregate, those steps take us toward the minimum of the loss. We can take advantage of the knowledge that we have accumulated from previous steps about where we should be headed. A cheap way to do that is to keep a Running Average of the gradients, and to use that running average instead of the direction of the current batch of the data. 

Running Average = M <- 0.9*M + Delta*Loss

This momentum technique works very well and often leads to better convergence. 

-

####Learning Rate Decay

When replacing gradient descent with SGD, we take smaller noisier steps towards our objective. But how small should that step be? 

It is beneficial to make that step smaller and smaller as you train. Some even like to apply an exponential decay to the learning rate. Some like making it smaller every time the loss reaches a plateau. There are lots of ways to go about it, but lowering it over time is the key thing to remember.
