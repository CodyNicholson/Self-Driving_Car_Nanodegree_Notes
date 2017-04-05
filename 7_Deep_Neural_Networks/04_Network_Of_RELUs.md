# Network Of RELUs

We currently have a logistic classifier:

> X * W + b = y

To turn this into a neural network (non-linear) we can simply add a RELU to the algorithm:

> X * W1 + b1 -> H RELUs -> (output of RELU) * W2 + b2 = y

We now have two matrices, one going from the inputs to the RELUs, and another one connecting the RELUs to the classifier

**H** is the number of RELUs that we have in the classifier. We can use H to add or subtract RELUs from our classifier.

***

### 2-Layer Neural Network

The first layer effectively consists of the set of weights and biases applied to X and passed through ReLUs. The output of this layer is fed to the next one, but is **not observable outside the network**, hence it is known as a **hidden layer**.

The second layer consists of the weights and biases applied to these intermediate outputs, followed by the softmax function to generate probabilities
