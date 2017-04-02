# TensorFlow Pooling Layer

### Using Pooling Layers in TensorFlow

In the below exercise, you'll be asked to set up the dimensions of the pooling filters, strides, as well as the appropriate padding. You should go over the TensorFlow documentation for **tf.nn.max_pool()**. Padding works the same as it does for a convolution.

##### Instructions

1. Finish off each **TODO** in the **maxpool** function.
2. Setup the **strides**, **padding** and **ksize** such that the output shape after pooling is **(1, 2, 2, 1)**.

quiz.py:

```python
"""
Set the values to `strides` and `ksize` such that
the output shape after pooling is (1, 2, 2, 1).
"""
import tensorflow as tf
import numpy as np

# `tf.nn.max_pool` requires the input be 4D (batch_size, height, width, depth)
# (1, 4, 4, 1)
x = np.array([
    [0, 1, 0.5, 10],
    [2, 2.5, 1, -8],
    [4, 0, 5, 6],
    [15, 1, 2, 3]], dtype=np.float32).reshape((1, 4, 4, 1))
X = tf.constant(x)

def maxpool(input):
    # TODO: Set the ksize (filter size) for each dimension (batch_size, height, width, depth)
    ksize = [?, ?, ?, ?]
    # TODO: Set the stride for each dimension (batch_size, height, width, depth)
    strides = [?, ?, ?, ?]
    # TODO: set the padding, either 'VALID' or 'SAME'.
    padding = ?
    # https://www.tensorflow.org/versions/r0.11/api_docs/python/nn.html#max_pool
    return tf.nn.max_pool(input, ksize, strides, padding)
    
out = maxpool(X)
```

***

### Solution

Here's how I did it. NOTE: there's more than 1 way to get the correct output shape. Your answer might differ from mine.

```python
def maxpool(input):
    ksize = [1, 2, 2, 1]
    strides = [1, 2, 2, 1]
    padding = 'VALID'
    return tf.nn.max_pool(input, ksize, strides, padding)
```

I want to transform the input shape **(1, 4, 4, 1)** to **(1, 2, 2, 1)**. I choose **'VALID'** for the padding algorithm. I find it simpler to understand and it achieves the result I'm looking for.

```
out_height = ceil(float(in_height - filter_height + 1) / float(strides[1]))
out_width  = ceil(float(in_width - filter_width + 1) / float(strides[2]))
```

Plugging in the values:

```
out_height = ceil(float(4 - 2 + 1) / float(2)) = ceil(1.5) = 2
out_width  = ceil(float(4 - 2 + 1) / float(2)) = ceil(1.5) = 2
```

The depth doesn't change during a pooling operation so I don't have to worry about that.
