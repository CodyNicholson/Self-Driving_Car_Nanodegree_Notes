### Hello, Tensor World! ###

import tensorflow as tf

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
	# Run the tf.constant operation in the session
	output = sess. run(hello_constant)
	print("\n")
	print(output)

"""
Tensor

In TensorFlow, data isn’t stored as integers, floats, or strings.
These values are encapsulated in an object called a tensor. In the
case of hello_constant = tf.constant('Hello World!'), hello_constant
is a 0-dimensional string tensor, but tensors come in a variety of
sizes as shown below:
"""

# A is a 0-dimensional int32 tensor
A = tf.constant(1234) 
# B is a 1-dimensional int32 tensor
B = tf.constant([123,456,789]) 
 # C is a 2-dimensional int32 tensor
C = tf.constant([ [123,456,789], [222,333,444] ])

"""
tf.constant() is one of many TensorFlow operations you will use in this
lesson. The tensor returned by tf.constant() is called a constant tensor,
because the value of the tensor never changes.
"""

"""
Session

TensorFlow’s api is built around the idea of a computational graph, a way
of visualizing a mathematical process which you learned about in the MiniFlow
lesson. Let’s take the TensorFlow code you ran and turn that into a graph:


A "TensorFlow Session", as shown above, is an environment for running a graph.
The session is in charge of allocating the operations to GPU(s) and/or CPU(s),
including remote machines. Let’s see how you use it.
"""

with tf.Session() as sess:
    output = sess.run(hello_constant)

"""
The code has already created the tensor, hello_constant, from the previous lines.
The next step is to evaluate the tensor in a session.

The code creates a session instance, sess, using tf.Session. The sess.run()
function then evaluates the tensor and returns the results.
"""
