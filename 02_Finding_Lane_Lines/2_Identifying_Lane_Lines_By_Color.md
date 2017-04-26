# Identifying Lane Lines By Color

To select a color we first need to think about what color actually means in the case of a digital image

In a digital image it means the stack of three images ([R,G,B]) that make up the colors of our image (Red, Green, Blue)

Each pixel of our image has three values each between 0 and 255 that represents the amount of each color that is in that pixel where 0 is the darkest shade of that color and 255 is the brightest shade of that color

Thus, the darkest pixel would be [0,0,0] and the brightest would be [255,255,255]

These three images that make up our single image are called **color channels**
