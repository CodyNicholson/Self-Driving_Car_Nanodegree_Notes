# Using the Hough Transform to find lines from Canny edges

After we take a gray scaled image and then use edge detection to turn it into an image full of dots, but only dots that represent edges in the original image. We now have to connect the dots. We can connect the dots to look for any kind of shape, but in this case we are looking for lane lines. To find lane lines we need to first adopt a model of a line and then fit that model to the assortment of dots in my edge detected image. Keeping in mind that my image is just a function of x any y, I can use equation of a line (Y = MX + B) to define the type of line I am looking for. In this case my model includes two parameters, M and B. In image space a line is plotted as X versus Y but in Parameter Space (Hough Space) I can represent that same line as M versus B instead. 

The **Hough Transform** is the conversion from **Image Space** to **Hough Space**

The characterization of a line in image space will be a single point at the position (M,B) in Hough Space

***

In image space, a line is plotted as x vs. y, but in 1962, Paul Hough devised a method for representing lines in parameter space, which we will call “Hough space” in his honor.

In Hough space, I can represent my "x vs. y" line as a point in "m vs. b" instead. The Hough Transform is just the conversion from image space to Hough space. So, the characterization of a line in image space will be a single point at the position (m, b) in Hough space.

So now I’d like to check your intuition… if a line in image space corresponds to a point in Hough space, what would two parallel lines in image space correspond to in Hough space?

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/houghQ1.png?raw=true)

**D** since parallel lines have the same slope, which is to say, the same “m” parameter in our line model. So, in parameter space, two parallel lines would be represented by two points at the same m value, but different b values.

***

Alright, so a line in image space corresponds to a point in Hough space. What does a point in image space correspond to in Hough space?

A single point in image space has many possible lines that pass through it, but not just any lines, only those with particular combinations of the m and b parameters. Rearranging the equation of a line, we find that a single point (x,y) corresponds to the line b = y - xm.

So what is the representation of a point in image space in Hough space?

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/houghQ2.png?raw=true)

**A** since a point in image space describes a line in Hough space. So a line in an image is a point in Hough space and a point in an image is a line in Hough space… cool!

***

What if you have 2 points in image space. What would that look like in Hough space?

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/houghQ3.png?raw=true)

**C** since two points in image space correspond to two lines in Hough Space. Not only that, but these lines must intersect

***

Alright, now we have two intersecting lines in Hough Space. How would you represent their intersection at the point (m0, b0) in image space?

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/houghQ4.png?raw=true)

**A** since the intersection point at (m0, b0) represents the line y = m0x + b0 in image space and it must be the line that passes through both points!

***

So, what happens if we run a Hough Transform on an image of a square? What will the corresponding plot in Hough space look like?

Our strategy to find lines in image space will be to will be to look for intersecting lines in Hough space. We do this by dividing up our Hough space into a grid and define intersecting lines as all lines passing through a given grid cell. To do this we will first run the Canny edge detection algorithm to find all the points associated with edges in my image. I can then consider every point in this edge detected image as a line in Hough space, and where many lines in Hough space intersect I declare that I have found a collection of points that described a line in image space. The problem is that vertical lines have infinite slope in (M,B) representation so we need a parameterization. Let's redefine our lne in polar coordinates. Now the variable row describes the perpendicular distance of the line from the origin and theta is the angle of the line away from horizontal. Now each point in image space corresponds to a sine curve in Hough space. If we take a whole line of points it translates into a whole bunch of sine curves in Hough space, and again the intersection of those sine curves in data row space give the parameterization of the line.

***

### Implementing a Hough Transform on Edge Detected Image

Now you know how the Hough Transform works, but to accomplish the task of finding lane lines, we need to specify some parameters to say what kind of lines we want to detect (i.e., long lines, short lines, bendy lines, dashed lines, etc.).

To do this, we'll be using an OpenCV function called HoughLinesP that takes several parameters. Let's code it up and find the lane lines in the image we detected edges in with the Canny function (for a look at coding up a Hough Transform from scratch, check this out.).

Here's the image we're working with:

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/houghEx1.jpg?raw=true)

Let's look at the input parameters for the OpenCV function HoughLinesP that we will use to find lines in the image. You will call it like this:

```python
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                                    min_line_length, max_line_gap)
```

In this case, we are operating on the image edges (the output from Canny) and the output from HoughLinesP will be lines, which will simply be an array containing the endpoints (x1, y1, x2, y2) of all line segments detected by the transform operation. The other parameters define just what kind of line segments we're looking for.

First off, **rho** and **theta** are the distance and angular resolution of our grid in Hough space. Remember that, in Hough space, we have a grid laid out along the (**theta**, ρ) axis. You need to specify **rho** in units of pixels and **theta** in units of radians.

So, what are reasonable values? Well, **rho** takes a minimum value of 1, and a reasonable starting place for theta is 1 degree (pi/180 in radians). Scale these values up to be more flexible in your definition of what constitutes a line.

The threshold parameter specifies the minimum number of votes (intersections in a given grid cell) a candidate line needs to have to make it into the output. The empty np.array([]) is just a placeholder, no need to change it. min_line_length is the minimum length of a line (in pixels) that you will accept in the output, and max_line_gap is the maximum distance (again, in pixels) between segments that you will allow to be connected into a single line. You can then iterate through your output lines and draw them onto the image to see what you got!

So, here's what its going to look like:

```python
# Do relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in and grayscale the image
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image)*0 #creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges)) 

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(combo)
```

![alt tag](https://github.com/CodyNicholson/Self-Driving_Car_Nanodegree/blob/master/2_Finding_Lane_Lines/houghEx2.jpg?raw=true)

As you can see I've detected lots of line segments!

***

### Example Of Tying It All Together

```python

```

Here's how I did it: I went with a low_threshold of 50 and high_threshold of 150 for Canny edge detection.

For region selection, I defined vertices = np.array([[(0,imshape[0]),(450, 290), (490, 290), (imshape[1],imshape[0])]], dtype=np.int32)

I chose parameters for my Hough space grid to be a rho of 2 pixels and theta of 1 degree (pi/180 radians). I chose a threshold of 15, meaning at least 15 points in image space need to be associated with each line segment. I imposed a min_line_length of 40 pixels, and max_line_gap of 20 pixels.
