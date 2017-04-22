#Computer Vision

Throughout this Nanodegree Program, we will be using Python with OpenCV for computer vision work. OpenCV stands for Open-Source Computer Vision. For now, you don't need to download or install anything, but later in the program we'll help you get these tools installed on your own computer.

OpenCV contains extensive libraries of functions that you can use. The OpenCV libraries are well documented, so if you’re ever feeling confused about what the parameters in a particular function are doing, or anything else, you can find a wealth of information at opencv.org.

***

###Canny Edge Detection

To detect the edges of objects in an image we first need to turn the image into greyscale (black & white), and then get the gradient of the image

By identifying edges, we can more easily detect objects based on their shape

```python
outputEdgesImg = cv2.Canny(inputImg, low_threshold, high_threshold)
```

low_threshold & high_threshold determine how strong the edges must be to be detected. The "strength" of an edge can be defined by looking at how different the values are in adjacent pixels in the image (the strength of the gradient).

-

Looking at a grayscale image you can see bright points, dark points, and all the gray in the middle. Rapid changes in brightness are where we find the edges. Our image is just a mathemetical function of x and y (f(x, y) = pixel value). By taking the derivative to measure the change in this function. Small derivatives denotes a small change, big derivitives denote big changes. Taking he derivative of X and Y simultaneously will provide us with the gradient. By computing the gradient we are measuring how fast pixels values are changing at each point in an image, and in which direction they are changing most rapidly. Computing the gradient gives us thick edges. With the Canny algorithm we will thin out these edges to find just the individual pixels that follow the strongest gradients. We will then extend those strong edges to include pixels all the way down to a lower threshold that we define when calling the Canny function.

**Note! The standard location of the origin (x=0, y=0) for images is in the top left corner with y values increasing downward and x increasing to the right. This might seem weird at first, but if you think about an image as a matrix, it makes sense that the "00" element is in the upper left.**

***

###Canny Edge Detection in Action

First, we need to read in an image:

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)
```

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/cannyAlgImg.jpg?raw=true)

Here we have an image of the road, and it's fairly obvious by eye where the lane lines are, but what about using computer vision?

Let's go ahead and convert to grayscale.

```python
import cv2  #bringing in OpenCV libraries
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
plt.imshow(gray, cmap='gray')
```

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/cannyAlgImgGray.jpg?raw=true)

Let’s try our Canny edge detector on this image. This is where OpenCV gets useful. First, we'll have a look at the parameters for the OpenCV Canny function. You will call it like this:

```python
edges = cv2.Canny(gray, low_threshold, high_threshold)
```

In this case, you are applying Canny to the image gray and your output will be another image called edges. low_threshold and high_threshold are your thresholds for edge detection.

The algorithm will first detect strong edge (strong gradient) pixels above the high_threshold, and reject pixels below the low_threshold. Next, pixels with values between the low_threshold and high_threshold will be included as long as they are connected to strong edges. The output edges is a binary image with white pixels tracing out the detected edges and black everywhere else. See the OpenCV Canny Docs for more details.

What would make sense as a reasonable range for these parameters? In our case, converting to grayscale has left us with an 8-bit image, so each pixel can take 2^8 = 256 possible values. Hence, the pixel values range from 0 to 255.

This range implies that derivatives (essentially, the value differences from pixel to pixel) will be on the scale of tens or hundreds. So, a reasonable range for your threshold parameters would also be in the tens to hundreds.

As far as a ratio of low_threshold to high_threshold, John Canny himself recommended a low to high ratio of 1:2 or 1:3.

We'll also include Gaussian smoothing, before running Canny, which is essentially a way of suppressing noise and spurious gradients by averaging (check out the OpenCV docs for GaussianBlur). cv2.Canny() actually applies Gaussian smoothing internally, but we include it here because you can get a different result by applying further smoothing (and it's not a changeable parameter within cv2.Canny()!).

You can choose the kernel_size for Gaussian smoothing to be any odd number. A larger kernel_size implies averaging, or smoothing, over a larger area. The example in the previous lesson was kernel_size = 3.

Note: If this is all sounding complicated and new to you, don't worry! We're moving pretty fast through the material here, because for now we just want you to be able to use these tools. If you would like to dive into the math underpinning these functions, please check out the free Udacity course, Intro to Computer Vision, where the third lesson covers Gaussian filters and the sixth and seventh lessons cover edge detection.

```python
#doing all the relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image and convert to grayscale
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
# Note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

# Define parameters for Canny and run it
# NOTE: if you try running this code you might want to change these!
low_threshold = 1
high_threshold = 10
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Display the image
plt.imshow(edges, cmap='Greys_r')
```

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/cannyAlgImgGradient.jpg?raw=true)

Here I've called the OpenCV function Canny on a Gaussian-smoothed grayscaled image called blur_gray and detected edges with thresholds on the gradient of high_threshold, and low_threshold.

In the next quiz you'll get to try this on your own and mess around with the parameters for the Gaussian smoothing and Canny Edge Detection to optimize for detecting the lane lines and not a lot of other stuff.

***

###Quiz

```python
# Do all the relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image and convert to grayscale
# Note: in the previous example we were reading a .jpg 
# Here we read a .png and convert to 0,255 bytescale
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 5 # Must be an odd number (3, 5, 7...)
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and run it
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Display the image
plt.imshow(edges, cmap='Greys_r')
```
