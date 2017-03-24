### Input ####

"""
In the last section, you passed a tensor into a session and it returned the result.
What if you want to use a non-constant? This is where tf.placeholder() and feed_dict come
into place. In this section, you'll go over the basics of feeding data into TensorFlow.
"""


## tf.placeholder() ##

"""
Sadly you can’t just set x to your dataset and put it in TensorFlow,
because over time you'll want your TensorFlow model to take in different datasets
with different parameters. You need tf.placeholder()!
"""

"""
tf.placeholder() returns a tensor that gets its value from data passed to the
tf.session.run() function, allowing you to set the input right before the session runs.
"""


## Session’s feed_dict ##

import tensorflow as tf

x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})


"""
Use the feed_dict parameter in tf.session.run() to set the placeholder tensor.
The above example shows the tensor x being set to the string "Hello, world".
It's also possible to set more than one tensor using feed_dict as shown below.
"""

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})

"""
Note: If the data passed to the feed_dict doesn’t match the tensor type and can’t
be cast into the tensor type, you’ll get the error “ValueError: invalid literal for...”.
"""


def run():
    output = None
    x = tf.placeholder(tf.int32)

    with tf.Session() as sess:
        output = sess.run(x, feed_dict={x: 123})

    return output

run()
