# Feature Extraction

The problem is that AlexNet was trained on the [ImageNet](http://www.image-net.org/) database, which has 1000 classes of images. You can see the classes in the **caffe_classes.py** file. None of those classes involves traffic signs.

In order to successfully classify our traffic sign images, you need to remove the final, 1000-neuron classification layer and replace it with a new, 43-neuron classification layer.

This is called feature extraction, because you're basically extracting the image features inferred by the penultimate layer, and passing these features to a new classification layer.

Open **feature_extraction.py** and complete the **TODO**(s).

Your output will probably not precisely match the sample output below, since the output will depend on the (probably random) initialization of weights in the network. That being said, the output classes you see should be present in **signnames.csv**.

```
Image 0
Double curve: 0.059
Ahead only: 0.048
Road work: 0.047
Dangerous curve to the right: 0.047
Road narrows on the right: 0.039

Image 1
General caution: 0.079
No entry: 0.067
Dangerous curve to the right: 0.054
Speed limit (50km/h): 0.053
Ahead only: 0.048

Time: 0.500 seconds
```

***

### Solution Code

```python
import time
import tensorflow as tf
import numpy as np
import pandas as pd
from scipy.misc import imread
from alexnet import AlexNet

sign_names = pd.read_csv('signnames.csv')
nb_classes = 43

x = tf.placeholder(tf.float32, (None, 32, 32, 3))
resized = tf.image.resize_images(x, (227, 227))

# Returns the second final layer of the AlexNet model,
# this allows us to redo the last layer specifically for 
# traffic signs model.
fc7 = AlexNet(resized, feature_extract=True)
shape = (fc7.get_shape().as_list()[-1], nb_classes)
fc8W = tf.Variable(tf.truncated_normal(shape, stddev=1e-2))
fc8b = tf.Variable(tf.zeros(nb_classes))
logits = tf.nn.xw_plus_b(fc7, fc8W, fc8b)
probs = tf.nn.softmax(logits)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# Read Images
im1 = imread("construction.jpg").astype(np.float32)
im1 = im1 - np.mean(im1)

im2 = imread("stop.jpg").astype(np.float32)
im2 = im2 - np.mean(im2)

# Run Inference
t = time.time()
output = sess.run(probs, feed_dict={x: [im1, im2]})

# Print Output
for input_im_ind in range(output.shape[0]):
    inds = np.argsort(output)[input_im_ind, :]
    print("Image", input_im_ind)
    for i in range(5):
        print("%s: %.3f" % (sign_names.ix[inds[-1 - i]][1], output[input_im_ind, inds[-1 - i]]))
    print()

print("Time: %.3f seconds" % (time.time() - t))
```

Here's how I did it:

```python
# Returns the second final layer of the AlexNet model,
# this allows us to redo the last layer specifically for 
# traffic signs model.
fc7 = AlexNet(resized, feature_extract=True)
shape = (fc7.get_shape().as_list()[-1], nb_classes)
fc8W = tf.Variable(tf.truncated_normal(shape, stddev=1e-2))
fc8b = tf.Variable(tf.zeros(nb_classes))
logits = tf.nn.xw_plus_b(fc7, fc8W, fc8b)
probs = tf.nn.softmax(logits)
```

First, I figure out the shape of the final fully connected layer, in my opinion this is the trickiest part. To do that I have to figure out the size of the output from **fc7**. Since it's a fully connected layer I know it's shape will be 2D so the second (or last) element of the list will be the size of the output. **fc7.get_shape().as_list()[-1]** does the trick. I then combine this with the number of classes for the Traffic Sign dataset to get the shape of the final fully connected layer, **shape = (fc7.get_shape().as_list()[-1], nb_classes)**. The rest of the code is just the standard way to define a fully connected in TensorFlow. Finally, I calculate the probabilities via softmax, **probs = tf.nn.softmax(logits)**.
