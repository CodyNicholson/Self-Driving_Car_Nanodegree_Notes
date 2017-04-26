# Forward Propagation

MiniFlow has two methods to help you define and then run values through your graphs: topological_sort() and forward_pass().

![alt tag](topoSort.jpg)

An example of topological sorting

In order to define your network, you'll need to define the order of operations for your nodes. Given that the input to some node depends on the outputs of others, you need to flatten the graph in such a way where all the input dependencies for each node are resolved before trying to run its calculation. This is a technique called a topological sort.

The topological_sort() function implements topological sorting using Kahn's Algorithm. The details of this method are not important, the result is; topological_sort() returns a sorted list of nodes in which all of the calculations can run in series. topological_sort() takes in a feed_dict, which is how we initially set a value for an Input node. The feed_dict is represented by the Python dictionary data structure. Here's an example use case:

```python
# Define 2 `Input` nodes.
x, y = Input(), Input()

# Define an `Add` node, the two above`Input` nodes being the input.
add = Add(x, y)

# The value of `x` and `y` will be set to 10 and 20 respectively.
feed_dict = {x: 10, y: 20}

# Sort the nodes with topological sort.
sorted_nodes = topological_sort(feed_dict=feed_dict)
```

-

The other method at your disposal is forward_pass(), which actually runs the network and outputs a value.

```python
def forward_pass(output_node, sorted_nodes):
    """
    Performs a forward pass through a list of sorted nodes.

    Arguments:

        `output_node`: The output node of the graph (no outgoing edges).
        `sorted_nodes`: a topologically sorted list of nodes.

    Returns the output node's value
    """

    for n in sorted_nodes:
        n.forward()

    return output_node.value
```

-

### Quiz 1 - Passing Values Forward

Create and run this graph!

![alt tag](addition-graph.png)

-

#### Setup

Review nn.py and miniflow.py.

The neural network architecture is already there for you in nn.py. It's your job to finish MiniFlow to make it work.

For this quiz, I want you to:

1. Open nn.py below. You don't need to change anything. I just want you to see how MiniFlow works.
2. Open miniflow.py. Finish the forward method on the Add class. All that's required to pass this quiz is a correct implementation of forward.
3. Test your network by hitting "Test Run!" When the output looks right, hit "Submit!"

nn.py:

```python
"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""

from miniflow import *

x, y = Input(), Input()

f = Add(x, y)

feed_dict = {x: 10, y: 5}

sorted_nodes = topological_sort(feed_dict)
output = forward_pass(f, sorted_nodes)

# NOTE: because topological_sort set the values for the `Input` nodes we could also access
# the value for x with x.value (same goes for y).
print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))
```

miniflow.py

```python
"""
You need to change the Add() class below.
"""

class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Nodes from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Nodes to which this Node passes values
        self.outbound_nodes = []
        # A calculated value
        self.value = None
        # Add this node as an outbound node on its inputs.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)

    # These will be implemented in a subclass.
    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_nodes` and
        store the result in self.value.
        """
        raise NotImplemented


class Input(Node):
    def __init__(self):
        # an Input node has no inbound nodes,
        # so no need to pass anything to the Node instantiator
        Node.__init__(self)

    # NOTE: Input node is the only node that may
    # receive its value as an argument to forward().
    #
    # All other node implementations should calculate their
    # values from the value of previous nodes, using
    # self.inbound_nodes
    #
    # Example:
    # val0 = self.inbound_nodes[0].value
    def forward(self, value=None):
        if value is not None:
            self.value = value


class Add(Node):
    def __init__(self, x, y):
        # You could access `x` and `y` in forward with
        # self.inbound_nodes[0] (`x`) and self.inbound_nodes[1] (`y`)
        Node.__init__(self, [x, y])

    def forward(self):
        """
        Set the value of this node (`self.value`) to the sum of it's inbound_nodes.

        Your code here!
        """
        
        self.value = self.inbound_nodes[0].value + self.inbound_nodes[1].value


"""
No need to change anything below here!
"""


def topological_sort(feed_dict):
    """
    Sort generic nodes in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` node and the value is the respective value feed to that node.

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


def forward_pass(output_node, sorted_nodes):
    """
    Performs a forward pass through a list of sorted nodes.

    Arguments:

        `output_node`: A node in the graph, should be the output node (have no outgoing edges).
        `sorted_nodes`: A topologically sorted list of nodes.

    Returns the output Node's value
    """

    for n in sorted_nodes:
        n.forward()

    return output_node.value

```

-

### Professor's Solution

Here's my solution (I'm just showing forward method of the Add class):

```python
def forward(self):
    x_value = self.inbound_nodes[0].value
    y_value = self.inbound_nodes[1].value
    self.value = x_value + y_value
```

While this looks simple, I want to show you why I used x_value and y_value from the inbound_nodes array. Let's take a look at the start with Node's constructor:

```python
class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this Node receives values.
        self.inbound_nodes = inbound_nodes
        # Removed everything else for brevity.
```

inbound_nodes are set when the Node is instantiated.

Of course, you weren't using Node directly, rather you used Add, which is a subclass of Node. Add's constructor is responsible for passing the inbound_nodes to Node, which happens here:

```python
class Add(Node):
    def __init__(self, x, y):
         Node.__init__(self, [x, y]) # calls Node's constructor
    ...
```

Lastly, there's the question of why node.value holds the value of the inputs. Take a look at the Input class to find out why.

```python
class Input(Node):
    ...

    # NOTE: Input node is the only node that may
    #  receive its value as an argument to forward().
    #
    # All other node implementations should calculate their
    # values from the value of previous nodes, using 
    # self.inbound_nodes
    #
    # Example:
    # val0 = self.inbound_nodes[0].value
    def forward(self, value=None):
        if value:
            self.value = value
```

For the Input node, the forward method appears to set the value.

That's not the case with other node subclasses, though. For those subclasses, the value is set when you run topological_sort. See here:

```python
def topological_sort(feed_dict):
    ...
    if isinstance(n, Input):
        n.value = feed_dict[n]
    ...
```

And that's it for addition!

Keep going to make MiniFlow more capable.
