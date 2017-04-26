# Cost

This is exciting! At this point, you have used weights and biases to compute outputs. And you've used an activation function to categorize the output. As you may recall, neural networks improve the accuracy of their outputs by modifying weights and biases in response to training against labeled datasets.

There are many techniques for defining the accuracy of a neural network, all of which center on the network's ability to produce values that come as close as possible to known correct values. People use different names for this accuracy measurement, often terming it loss or cost. I'll use the term cost most often.

For this lab, you will calculate the cost using the mean squared error (MSE). It looks like so:

![alt tag](costEquation.png)

Equation (5)

Here w denotes the collection of all weights in the network, b all the biases, m is the total number of training examples, a is the approximation of y(x) by the network, both a and y(x) are vectors of the same length.

The collection of weights is all the weight matrices flattened into vectors and concatenated to one big vector. The same goes for the collection of biases except they're already vectors so there's no need to flatten them prior to the concatenation.

Here's an example of creating w in code:

```python
# 2 by 2 matrices
w1  = np.array([[1, 2], [3, 4]])
w2  = np.array([[5, 6], [7, 8]])

# flatten
w1_flat = np.reshape(w1, -1)
w2_flat = np.reshape(w2, -1)

w = np.concatenate((w1_flat, w2_flat))
# array([1, 2, 3, 4, 5, 6, 7, 8])
```

It's a nice way to abstract all the weights and biases used in the neural network and makes some things easier to write as we'll see soon in the upcoming gradient descent sections.

NOTE: It's not required you do this in your code! It's just easier to do this talk about the weights and biases as a collective than consider them individually.

The cost, C, depends on the difference between the correct output, y(x), and the network's output, a. It's easy to see that no difference between y(x) and a (for all values of x) leads to a cost of 0.

This is the ideal situation, and in fact the learning process revolves around minimizing the cost as much as possible.

I want you to calculate the cost now.

You implemented this network in the forward direction in the last quiz.

As it stands right now, it outputs gibberish. The activation of the sigmoid node means nothing because the network has no labeled output against which to compare. Furthermore, the weights and bias cannot change and learning cannot happen without a cost.

***

### Code:

nn.py:

```python
"""
Test your MSE method with this script!

No changes necessary, but feel free to play
with this script to test your network.
"""

import numpy as np
from miniflow import *

y, a = Input(), Input()
cost = MSE(y, a)

y_ = np.array([1, 2, 3])
a_ = np.array([4.5, 5, 10])

feed_dict = {y: y_, a: a_}
graph = topological_sort(feed_dict)
# forward pass
forward_pass(graph)

"""
Expected output

23.4166666667
"""
print(cost.value)
```

miniflow.py:

```python
import numpy as np


class Node(object):
    """
    Base class for nodes in the network.

    Arguments:

        `inbound_nodes`: A list of nodes with edges into this node.
    """
    def __init__(self, inbound_nodes=[]):
        """
        Node's constructor (runs when the object is instantiated). Sets
        properties that all nodes need.
        """
        # A list of nodes with edges into this node.
        self.inbound_nodes = inbound_nodes
        # The eventual value of this node. Set by running
        # the forward() method.
        self.value = None
        # A list of nodes that this node outputs to.
        self.outbound_nodes = []
        # Sets this node as an outbound node for all of
        # this node's inputs.
        for node in inbound_nodes:
            node.outbound_nodes.append(self)

    def forward(self):
        """
        Every node that uses this class as a base class will
        need to define its own `forward` method.
        """
        raise NotImplementedError


class Input(Node):
    """
    A generic input into the network.
    """
    def __init__(self):
        # The base class constructor has to run to set all
        # the properties here.
        #
        # The most important property on an Input is value.
        # self.value is set during `topological_sort` later.
        Node.__init__(self)

    def forward(self):
        # Do nothing because nothing is calculated.
        pass


class Linear(Node):
    """
    Represents a node that performs a linear transform.
    """
    def __init__(self, X, W, b):
        # The base class (Node) constructor. Weights and bias
        # are treated like inbound nodes.
        Node.__init__(self, [X, W, b])

    def forward(self):
        """
        Performs the math behind a linear transform.
        """
        X = self.inbound_nodes[0].value
        W = self.inbound_nodes[1].value
        b = self.inbound_nodes[2].value
        self.value = np.dot(X, W) + b


class Sigmoid(Node):
    """
    Represents a node that performs the sigmoid activation function.
    """
    def __init__(self, node):
        # The base class constructor.
        Node.__init__(self, [node])

    def _sigmoid(self, x):
        """
        This method is separate from `forward` because it
        will be used with `backward` as well.

        `x`: A numpy array-like object.
        """
        return 1. / (1. + np.exp(-x))

    def forward(self):
        """
        Perform the sigmoid function and set the value.
        """
        input_value = self.inbound_nodes[0].value
        self.value = self._sigmoid(input_value)


class MSE(Node):
    def __init__(self, y, a):
        """
        The mean squared error cost function.
        Should be used as the last node for a network.
        """
        # Call the base class' constructor.
        Node.__init__(self, [y, a])

    def forward(self):
        """
        Calculates the mean squared error.
        """
        # NOTE: We reshape these to avoid possible matrix/vector broadcast
        # errors.
        #
        # For example, if we subtract an array of shape (3,) from an array of shape
        # (3,1) we get an array of shape(3,3) as the result when we want
        # an array of shape (3,1) instead.
        #
        # Making both arrays (3,1) insures the result is (3,1) and does
        # an elementwise subtraction as expected.
        # MY CODE HERE
        y = self.inbound_nodes[0].value.reshape(-1, 1)
        a = self.inbound_nodes[1].value.reshape(-1, 1)
        m = self.inbound_nodes[0].value.shape[0]

        diff = y - a
        self.value = np.mean(diff**2)


def topological_sort(feed_dict):
    """
    Sort the nodes in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` Node and the value is the respective value feed to that Node.

    Returns a list of sorted nodes.
    """

    input_nodes = [n for n in feed_dict.keys()]

    G = {}
    nodes = [n for n in input_nodes]
    while len(nodes) > 0:
        n = nodes.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_nodes:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            nodes.append(m)

    L = []
    S = set(input_nodes)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_nodes:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L


def forward_pass(graph):
    """
    Performs a forward pass through a list of sorted Nodes.

    Arguments:

        `graph`: The result of calling `topological_sort`.
    """
    # Forward pass
    for n in graph:
        n.forward()

```

The math behind MSE reflects Equation (5), where y is target output and a is output computed by the neural network. We then square the difference diff**2, alternatively, this could be np.square(diff). Lastly we need to sum the squared differences and divide by the total number of examples m. This can be achieved in with np.mean or (1 /m) * np.sum(diff**2).

Note the order of y and a doesn't actually matter, we could switch them around (a - y) and get the same value.
