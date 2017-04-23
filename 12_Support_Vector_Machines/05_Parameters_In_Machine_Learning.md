# Parameters In Machine Learning

Parameters are arguments that you pass when you create your classifier, before fitting. They can make a huge difference in the decision boundary that your algorithm arrives at.

##### What are the parameters for an SVM

There is the **kernel**, which we already covered. Then there is also **c** and **gamma**. 

### The C Parameter

The **c** parameter controls the tradeoff between a smooth decision decision boundary and classifying training points correctly

A large value of **c** means that you're going to get more training points correct - you get a more intricate decision boundary. A small **c** value will draw a more smooth/linear decision boundary that will not be as accurate in classifying the training data.

### The Gamma Parameter

**Gamma** defines how far the influence of a single training example reaches. If gamma has a low value, then that means that every point has a far reach. High values means that each training point example only has a close reach.

A high gamma value will not take into consideration points that are far away from the decision boundary, only those points that are close to it. A low gamma value will take into consideration these far away values and the close values as well. 

This being said, with a high gamma value points closer to the decision boundary will influence it more. They have more weight in the decision making process. 

The 'gamma' parameter actually has no effect on the 'linear' kernel for SVMs. The key parameter for this kernel function is "C", which is described on the following video.
