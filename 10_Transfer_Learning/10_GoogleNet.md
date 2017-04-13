# GoogLeNet

In 2014 google published its own network in the ImageNet competition called GoogLeNet that has a loss ratio of 6.7%, a little better than VGG at 7.3%

GoogLeNet's great advantage is that it runs really fast. The team that developed googLeNet developed a clever concept called an **inception module** which trains really well and is efficiently deployable.

In an **Inception Module** at each layer of your CovNet you can make a choice to either have a pooling operation or have a convolution of some size (1x1, 3x3, 5x5?). Instead of having a single convolution, you have a composition of average cooling followed by 1x1. Then a 1x1 convolution followed by a 3x3. Then a 1x1 followed by a 5x5. At the top of the network you simply concatenate the output of each of the steps. You can choose the parameters in such a way that the total number of parameters in your model is very small, yet the model performs better than if you had a single convolution.

The inception modules create a situation in which the total number of parameters is very small. This is why googLeNet runs almost as fast as AlexNet. GoogLeNet is a great choice to investigate if you need your algorithm to choose if you need your network to run in real time, like maybe in a self-driving car!
