#Sigmoid Neural Network Sketch

###Sigmoid

Sigmoid is a function that makes an "S" shape when plotted on a graph. 

The Sigmoid of an Activation "a" is equal to: (1/(1+e^-a))

As activation becomes less, we will go towards 0, and as it rises we will go towards 1

***

###Neural Network

We can construct a neural network using Sigmoid Units, a chain of relationships between input layer (The different components of x) and the output (y). The way this will happen is that there are other layers of units in-between that are each computing the weighted sum, sigmoided, of the layer before it. These other layers of units (between the output and the input) are referred to as hidden layers.

Each unit is taking the weights and multiplying by the inputs. putting it through the sigmoid, and resulting in the output activation.

This mapping from input to output is differentiable in terms of the weights. We can figure out for any given weight in the network how moving it up or down a little bit is going to change the mapping from inputs to outputs. So we can move all those weights in the direction of producing more like the output that we want. Even though there are many non-linearities in-between. This leads to **Back Propagation**. - computationally beneficial organization of the chain rule.

We have information flowing from the inputs to the outputs, but we also have error information flowing back from the outputs towards the inputs that tells you how to compute all the derivatives and then, therefore, how to make all the weight updates to make the network produce something more like what you wanted. The algorithm learns.

This works as long as the function is differentiable. 

Sometimes there are multiple local optimums. You might need to change more than just one weight at a time to get to the most optimum solution.

***
