### TensorFlow Math ###

"""
Getting the input is great, but now you need to use it. You're going to use basic math
functions that everyone knows and loves - add, subtract, multiply, and divide - with
tensors. (There's many more math functions you can check out in the documentation.)
"""

## Addition ##

import tensorflow as tf

a = tf.add(5, 2)  # 7

"""
You’ll start with the add function. The tf.add() function does exactly what you expect
it to do. It takes in two numbers, two tensors, or one of each, and returns their sum
as a tensor.
"""


## Subtraction and Multiplication ##

s = tf.subtract(10, 4) # 6
m = tf.multiply(2, 5)  # 10

"""
The x tensor will evaluate to 6, because 10 - 4 = 6. The y tensor will evaluate to 10,
because 2 * 5 = 10. That was easy!
"""


## Converting Types ##

"""
It may be necessary to convert between types to make certain operators work together.
For example, if you tried the following, it would fail with an exception:
"""

tf.subtract(tf.constant(2.0),tf.constant(1))

# Fails with ValueError: Tensor conversion requested dtype float32 for Tensor with dtype int32:

"""
That's because the constant 1 is an integer but the constant 2.0 is a floating point value
and subtract expects them to match.

In cases like these, you can either make sure your data is all of the same type, or you can 
ast a value to another type. In this case, converting the 2.0 to an integer before
subtracting, like so, will give the correct result:
"""

tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   # 1



# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x1 = 10
y1 = 2
z1 = x1/y1 - 1

x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x,y),1)

# TODO: Print z from a session

with tf.Session() as sess:
    output = sess.run(z)
    print("\n")
    print(output)
