# TensorFlow Convolution Layer

#### Using Convolution Layers in TensorFlow

Let's now apply what we've learned to build real CNNs in TensorFlow. In the below exercise, you'll be asked to set up the dimensions of the Convolution filters, the weights, the biases. This is in many ways the trickiest part to using CNNs in TensorFlow. Once you have a sense of how to set up the dimensions of these attributes, applying CNNs will be far more straight forward.

#### Review

You should go over the TensorFlow documentation for [2D convolutions](https://www.tensorflow.org/api_guides/python/nn#Convolution). Most of the documentation is straightforward, except perhaps the **padding** argument. The padding might differ depending on whether you pass **'VALID'** or **'SAME'**.

Here are a few more things worth reviewing:

- Introduction to TensorFlow -> TensorFlow Variables.
- How to determine the dimensions of the output based on the input size and the filter size (shown below). You'll use this to determine what the size of your filter should be.

```python
 new_height = (input_height - filter_height + 2 * P)/S + 1
 new_width = (input_width - filter_width + 2 * P)/S + 1
```

#### Instructions

1. Finish off each **TODO** in the **conv2d** function.
2. Setup the **strides**, **padding** and filter weight/bias (**F_w** and **F_b**) such that the output shape is **(1, 2, 2, 3)**. Note that all of these except **strides** should be TensorFlow variables.

quiz.py:

```
"""
Setup the strides, padding and filter weight/bias such that
the output shape is (1, 2, 2, 3).
"""
import tensorflow as tf
import numpy as np

# `tf.nn.conv2d` requires the input be 4D (batch_size, height, width, depth)
# (1, 4, 4, 1)
x = np.array([
    [0, 1, 0.5, 10],
    [2, 2.5, 1, -8],
    [4, 0, 5, 6],
    [15, 1, 2, 3]], dtype=np.float32).reshape((1, 4, 4, 1))
X = tf.constant(x)


def conv2d(input):
    # Filter (weights and bias)
    # The shape of the filter weight is (height, width, input_depth, output_depth)
    # The shape of the filter bias is (output_depth,)
    # TODO: Define the filter weights `F_W` and filter bias `F_b`.
    # NOTE: Remember to wrap them in `tf.Variable`, they are trainable parameters after all.
    F_W = tf.Variable(tf.truncated_normal((2, 2, 1, 3)))
    F_b = tf.Variable(tf.zeros(3))
    # TODO: Set the stride for each dimension (batch_size, height, width, depth)
    strides = [1, 2, 2, 1]
    # TODO: set the padding, either 'VALID' or 'SAME'.
    padding = 'VALID'
    # https://www.tensorflow.org/versions/r0.11/api_docs/python/nn.html#conv2d
    # `tf.nn.conv2d` does not include the bias computation so we have to add it ourselves after.
    return tf.nn.conv2d(input, F_W, strides, padding) + F_b

out = conv2d(X)
```

output:

```
Output shape: [1, 2, 2, 3]
Convolution result: [[[[ -2.24282789   1.10420561  -4.42264605]
   [  7.13450527 -11.99885368   1.23035717]]

  [[ -8.07241917 -11.08131409   5.97849512]
   [ -0.36686254  -3.00977993 -10.94535923]]]]
```

***

###Solution

Here's how I did it. NOTE: there's more than 1 way to get the correct output shape. Your answer might differ from mine.

```python
def conv2d(input):
    # Filter (weights and bias)
    F_W = tf.Variable(tf.truncated_normal((2, 2, 1, 3)))
    F_b = tf.Variable(tf.zeros(3))
    strides = [1, 2, 2, 1]
    padding = 'VALID'
    return tf.nn.conv2d(input, F_W, strides, padding) + F_b
```

I want to transform the input shape **(1, 4, 4, 1)** to **(1, 2, 2, 3)**. I choose **'VALID'** for the padding algorithm. I find it simpler to understand and it achieves the result I'm looking for.

```
out_height = ceil(float(in_height - filter_height + 1) / float(strides[1]))
out_width  = ceil(float(in_width - filter_width + 1) / float(strides[2]))
```

Plugging in the values:

```
out_height = ceil(float(4 - 2 + 1) / float(2)) = ceil(1.5) = 2
out_width  = ceil(float(4 - 2 + 1) / float(2)) = ceil(1.5) = 2
```

In order to change the depth from 1 to 3, I have to set the output depth of my filter appropriately:

```
F_W = tf.Variable(tf.truncated_normal((2, 2, 1, 3))) # (height, width, input_depth, output_depth)
F_b = tf.Variable(tf.zeros(3)) # (output_depth)
```

The input has a depth of 1, so I set that as the **input_depth** of the filter.
