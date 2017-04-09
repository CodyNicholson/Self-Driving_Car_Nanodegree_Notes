# ImageNet

The internet has made it easier to generate and collect images. Storage costs had dropped so that it was cheap to save large collections of images and services like amazon's mechanical turk had made it even more cost effective to label images. That confluence of factors gave rise to **ImageNet**, a huge database of hand labeled images.

The ImageNet database gave rise to the image net large-scale visual recognition competition. The ImageNet large-scale visual recognition competition is most famous as an annual competition where teams from industry and academia try to build the best network for object detection and localization. This intense competition between teams from industry and academia produced some of the best image classification networks. In 2012 *AlexNet* was created, and it looked a lot like LeNet. 

AlexNet, while looking a lot like LeNet, was a breakthrough in several respects. First, AlexNet used a massive parallelism afforded by GPUs to accelerate training using the best GPUs. Using the best GPUs, AlexNet was able to train in about a week. Additionally, AlexNet pioneered the use of rectified linear units as an activation function, and dropout as a technique for avoiding overfitting.

In 2011 - the year before AlexNet was developed - the winner of the ImageNet competition successfully classified 74% of images. Or, in the terminology of the competition, it's error was 26%. The next year AlexNet lowered it's error to 15% which was a huge leap forward.

***

### AlexNet Architecture

AlexNet puts the network on two GPUs, which allows for building a larger network. Although most of the calculations are done in parallel, the GPUs communicate with each other in certain layers. The original research paper on AlexNet said that parallelizing the network decreased the classification error rate by 1.7% when compared to a neural network that used half as many neurons on one GPU.

![alt tag](alexNet.png)
