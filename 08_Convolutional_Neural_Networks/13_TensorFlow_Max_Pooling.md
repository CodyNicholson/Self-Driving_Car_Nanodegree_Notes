# TensorFlow Max Pooling

![alt tag](max-pooling.png)

By Aphex34 (Own work) [CC BY-SA 4.0 (http://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons

The image above is an example of [max pooling](https://en.wikipedia.org/wiki/Convolutional_neural_network#Pooling_layer) with a 2x2 filter and stride of 2. The four 2x2 colors represent each time the filter was applied to find the maximum value.

For example, **[[1, 0], [4, 6]]** becomes **6**, because **6** is the maximum value in this set. Similarly, **[[2, 3], [6, 8]]** becomes **8**.

Conceptually, the benefit of the max pooling operation is to reduce the size of the input, and allow the neural network to focus on only the most important elements. Max pooling does this by only retaining the maximum value for each filtered area, and removing the remaining values.

TensorFlow provides the **tf.nn.max_pool()** function to apply [max pooling](https://en.wikipedia.org/wiki/Convolutional_neural_network#Pooling_layer) to your convolutional layers.

```python
...
conv_layer = tf.nn.conv2d(input, weight, strides=[1, 2, 2, 1], padding='SAME')
conv_layer = tf.nn.bias_add(conv_layer, bias)
conv_layer = tf.nn.relu(conv_layer)
# Apply Max Pooling
conv_layer = tf.nn.max_pool(
    conv_layer,
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding='SAME')
```

The **tf.nn.max_pool()** function performs max pooling with the **ksize** parameter as the size of the filter and the **strides** parameter as the length of the stride. 2x2 filters with a stride of 2x2 are common in practice.

The **ksize** and **strides** parameters are structured as 4-element lists, with each element corresponding to a dimension of the input tensor **([batch, height, width, channels])**. For both **ksize** and **strides**, the batch and channel dimensions are typically set to **1**.
