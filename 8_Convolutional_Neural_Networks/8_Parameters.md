# Parameter Sharing

![alt tag](covnetCats.png)

The weights, w, are shared across patches for a given layer in a CNN to detect the cat above regardless of where in the image it is located.

When we are trying to classify a picture of a cat, we don’t care where in the image a cat is. If it’s in the top left or the bottom right, it’s still a cat in our eyes. We would like our CNNs to also possess this ability known as translation invariance. How can we achieve this?

As we saw earlier, the classification of a given patch in an image is determined by the weights and biases corresponding to that patch.

If we want a cat that’s in the top left patch to be classified in the same way as a cat in the bottom right patch, we need the weights and biases corresponding to those patches to be the same, so that they are classified the same way.

This is exactly what we do in CNNs. The weights and biases we learn for a given output layer are shared across all patches in a given input layer. Note that as we increase the depth of our filter, the number of weights and biases we have to learn still increases, as the weights aren't shared across the output channels.

There’s an additional benefit to sharing our parameters. If we did not reuse the same weights across all patches, we would have to learn new parameters for every single patch and hidden layer neuron pair. This does not scale well, especially for higher fidelity images. Thus, sharing parameters not only helps us with translation invariance, but also gives us a smaller, more scalable model.

### Padding

![alt tag](a5x5gridWith3x3Filter.png)

A 5x5 grid with a 3x3 filter. Source: Andrej Karpathy.

Let's say we have a 5x5 grid (as shown above) and a filter of size 3x3 with a stride of 1. What's the width and height of the next layer? We see that we can fit at most three patches in each direction, giving us a dimension of 3x3 in our next layer. As we can see, the width and height of each subsequent layer decreases in such a scheme.

In an ideal world, we'd be able to maintain the same width and height across layers so that we can continue to add layers without worrying about the dimensionality shrinking and so that we have consistency. How might we achieve this? One way is to simply add a border of 0s to our original 5x5 image. You can see what this looks like in the below image.

![alt tag](girdWith0padding.png)

The same grid with 0 padding. Source: Andrej Karpathy.

This would expand our original image to a 7x7. With this, we now see how our next layer's size is again a 5x5, keeping our dimensionality consistent.

### Dimensionality

From what we've learned so far, how can we calculate the number of neurons of each layer in our CNN?

Given:

- our input layer has a width of **W** and a height of **H**
- our convolutional layer has a filter size **F**
- we have a stride of **S**
- a padding of **P**
- and the number of filters **K**

The following formula gives us the width of the next layer: **W_out = (W−F+2P)/S+1**

The output height would be **H_out = (H-F+2P)/S + 1**

And the output depth would be equal to the number of filters **D_out = K**

The output volume would be **W_out * H_out * D_out**

Knowing the dimensionality of each additional layer helps us understand how large our model is and how our decisions around filter size and stride affect the size of our network.

***

### Quiz - Convolutional Layer Output Shape

For the next few quizzes we'll test your understanding of the dimensions in CNNs. Understanding dimensions will help you make accurate tradeoffs between model size and performance. As you'll see, some parameters have a much bigger impact on model size than others.

### Setup

H = height, W = width, D = depth

- We have an input of shape 32x32x3 (HxWxD)
- 20 filters of shape 8x8x3 (HxWxD)
- A stride of 2 for both the height and width (S)
- With padding of size 1 (P)

Recall the formula for calculating the new height or width:

```
new_height = (input_height - filter_height + 2 * P)/S + 1
new_width = (input_width - filter_width + 2 * P)/S + 1
```

####Convolutional Layer Output Shape

What's the shape of the output?

The answer is 14x14x20

We can get the new height and width with the above formula resulting in:

```
(32 - 8 + 2 * 1)/2 + 1 = 14
(32 - 8 + 2 * 1)/2 + 1 = 14
```

The new depth is equal to the number of filters, which is 20

***

This would correspond to the following code:

```python
input = tf.placeholder(tf.float32, (None, 32, 32, 3))
filter_weights = tf.Variable(tf.truncated_normal((8, 8, 3, 20))) # (height, width, input_depth, output_depth)
filter_bias = tf.Variable(tf.zeros(20))
strides = [1, 2, 2, 1] # (batch, height, width, depth)
padding = 'SAME'
conv = tf.nn.conv2d(input, filter_weights, strides, padding) + filter_bias
```

Note the output shape of conv will be [1, 16, 16, 20]. It's 4D to account for batch size, but more importantly, it's not [1, 14, 14, 20]. This is because the padding algorithm TensorFlow uses is not exactly the same as the one above. An alternative algorithm is to switch padding from 'SAME' to 'VALID' which would result in an output shape of [1, 13, 13, 20]. If you're curious how padding works in TensorFlow, read this document.

In summary TensorFlow uses the following equation for 'SAME' vs 'PADDING'

**SAME Padding**, the output height and width are computed as:

out_height = ceil(float(in_height) / float(strides1))

out_width = ceil(float(in_width) / float(strides[2]))

**VALID Padding**, the output height and width are computed as:

out_height = ceil(float(in_height - filter_height + 1) / float(strides1))

out_width = ceil(float(in_width - filter_width + 1) / float(strides[2]))
