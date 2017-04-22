# Keras Overview

[Keras](https://keras.io/) makes coding deep neural networks simpler. To demonstrate just how easy it is, you're going to build a simple fully-connected network in a few dozen lines of code.

We’ll be connecting the concepts that you’ve learned in the previous lessons to the methods that Keras provides.

The network you will build is similar to Keras’s [sample network](https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py) that builds out a convolutional neural network for [MNIST](http://yann.lecun.com/exdb/mnist/). However for the network you will build you're going to use a small subset of the [German Traffic Sign Recognition Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news) dataset that you've used previously.

The general idea for this example is that you'll first load the data, then define the network, and then finally train the network.
