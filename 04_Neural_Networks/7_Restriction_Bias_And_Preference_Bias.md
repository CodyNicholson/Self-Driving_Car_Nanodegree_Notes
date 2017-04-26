# Restriction Bias & Preference Bias

Restriction Bias tells you something about the representational power of whatever data structure it is that you are using. So in this case, the network of neurons. It also tells you the set of hypothesis that you are willing to consider. If there is a great deal of restriction, then there is lots of different kinds of models that were  not even considered. We are restricting our view to just a subset of those. In the case of neural nets, the restrictions we will use are: Linear Perceptron Units (half space planes), Sigmoids (much more complex, not much restriction).

We can add restrictions to:

- Boolean Functions: If we have a complex enough network with enough units we can map almost all the different subcomponents of any boolean expression to threshold-like units and build a circuit that can compute whatever boolean function we want.
- Continuous Functions (As the input changes, the output changes smoothly): As long as it is connected (has no jumps) we can do this with just a single hidden layer as long as it has enough units.
- Arbitrary Functions: We can still represent this with a neural network. Any mapping from the input to the outputs we can represent with a neural network, even if discontinuous, just by adding one more hidden layer. This gives us the ability to not just stitch together these patches, but also to have big jumps between the patches. More complex Neural Nets or more vulnerable to over-fitting. 

Neural Networks are not restricted in terms of their bias as long as you have a sufficiently complex network structure, possibly having multiple hidden layers. 

Use Cross Validation to avoid over-fitting

***

### Preference Bias

Preference Bias tells you what it is you are able to represent. It tells you about the algorithm that you are using to learn. It tells you, given two representations, why I would prefer one over the other. 

Preference Bias tells us what algorithm to use, the initial weights to start with.

It is typical to start your weights at small random values. It give it some variability since it is random. We won't have to worry about getting stuck in the same spot twice since it will be random data each iteration. It is important to start with small values to avoid over-fitting, we will start with low complexity with simpler explanations. 

**Occam's Razor**: Entities should not be multiplied unnecessarily. 

If we are not doing any better fitting the data, then we should not multiply entities. "Multiply" meaning: make more complex. Do not make more complex unless it causes less error. Choose the simpler solution, use the one that is less complex.
