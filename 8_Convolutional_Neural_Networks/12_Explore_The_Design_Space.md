# Explore The Design Space

Now that we have seen what a simple covnet looks like, there are many things that we can do to improve it. Namely, we will talk about three of them:

- Pooling
- 1x1 Convolutions
- Inception Architecture

***

### Pooling

The first improvement, pooling, is a better way to reduce the spacial extent of your feature maps in the convolutional pyramid. Until now, we have used striding to shift the filters by a few pixels each time and reduce the feature map size. This is a very aggressive way to downsample an image. it removes a lot of information. What if instead of skipping one in every two convolutions, we still ran with a very small stride, say for example one, but then took all the convolutions in the neighborhood and combined them somehow. That operation is called **Pooling**, and there are a few ways to go about it. 

The most common way to use pooling is in **Max Pooling**. At every point on the feature map, look at a small neighborhood around that point and compute the maximum of all the responses around it. There are some advantages to using Max Pooling. First, it does not add to your number of parameters so you don't risk an increase in overfitting. Second, it often yields more accurate models.

However, since the convolutions that run below run at a lower stride, the model then becomes a lot more expensive to compute. Now you have even more to hyper-parameters to worry about: the pooling region size, and the pooling stride. These hyper-parameters do not need to be the same.

A very typical architecture for a covnet is a few layers alternating convolutions and max pooling, followed by a few fully connected layers at the top. The first famous model to use this architecture was the LENET-5 designed by Yann Lecun to the character recognition back in 1998. Modern convolutional networks such as ALEXNET, which was creased by Alex Krizhevsky in 2012 famously won the competitive ImageNet object recognition challenge in 2012, used a very similar architecture with a few wrinkles. 

***

### Average Pooling

Anther notable form of pooling is **Average Pooling**. Instead of taking the max, it takes the average over the window of pixels around a specific location. It's a little bit like providing a blurred low resolution view of the feature map. 
