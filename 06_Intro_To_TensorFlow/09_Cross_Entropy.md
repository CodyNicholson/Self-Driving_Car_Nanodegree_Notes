# Cross Entropy (Distance)

One-hot encoding works well until you have tons of different classes. This is because if you have lots of classes then you will have lots of encoded values - a vector with as many encoded values as you have classes for each class. Each class's vector of encoded values will have only a single "1" and the reset of the values will be "0" since there can only be one correct label. This becomes very inefficient.

We can tell how well we are doing by simply comparing two vectors - the one that comes out of the classifier that contains the probabilities of the classes, and the one-hot encoded vectors that corresponds to the labels.

The way that we measure the distance between those two probability vectors is called the **Cross-Entropy** (denoted "D" in the equation for "distance"). The equation for finding this distance is:

#### D(S,L) = -(Summation i(L_i * log(S_i)))

Where S is the outputted vector of probabilities from the Softmax equation, and L is the vector of hot-encoded labels.

***

### Quiz

![alt tag](cross-entr.png)

###### Cross Entropy Function (S = Softmax, L = One-Hot Encoded Labels)

Let's take what you learned from the video and create a cross entropy function in TensorFlow. To create a cross entropy function in TensorFlow, you'll need to use two new functions:

- tf.reduce_sum()
- tf.log()

***

#### Reduce Sum

```python
x = tf.reduce_sum([1, 2, 3, 4, 5])  # 15
```

The tf.reduce_sum() function takes an array of numbers and sums them together.

***

#### Natural Log

```python
x = tf.log(100)  # 4.60517
```

This function does exactly what you would expect it to do. tf.log() takes the natural log of a number.

***

```python
# Solution is available in the other "solution.py" tab
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO: Print cross entropy from session

cross_entropy = -tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

with tf.Session() as sess:
    print(sess.run(cross_entropy, feed_dict={softmax: softmax_data, one_hot: one_hot_data}))

```
