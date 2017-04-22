#Regression & Function Approximation

In supervised learning we are going to take examples of inputs and outputs. Now given a new input, we will predict its output.

Regression is the process of mapping continuous inputs to outputs - Discrete and continuous

***

###Functional Approximation

Using functional form to approximate a bunch of data points. For example, heights of kids based on their parents. A tall parent (relative to the set of all people) will likely have a kid that is taller than the normal person, but shorter than them. A short parent will likely have a kid that is taller than them, but short in relative to the average person. On a graph we can use regression to predict the heights of kids based on their parents and the averge height of a person.

***

###Linear Regression

Linear regression is very simple to visualize. Using a function we can draw a line through the data points listed on a graph (cartesian plane). Ideally our function will draw a line that will represent the average of all the data at all positions of the graph. We find the best line on this graph using calculus. We will use this function:

```
f(x) = (C0 * x^0) + (C1 * x^1) + (C2 * x^2) + ... + (Ck * x^k)
```

K values correspond to:

```
k=0, constant
k=1, line
k=2, parabola
k=3, cubic
k=8, octic
```

Using k= 0 it will draw a constant, horizontal line on a graph of many points to represent the average of just the y-axis. This is bad because it doesn't tell us much about the data.

Using k=1 it will draw a straight line through the data points that represents the average of both the y and x axis. Still doesn't tell us as much as we need to know about the data points, the average of all isn't specific enough.

Using k=2 it will draw a line with a single curve through all the data points representing the average at every point in the graph. This is the best so far, but thatit still could be better.

Using k=3 our line will have multiple curves that adjust to the data points without too closely following them. If we continued to increment k our data points would be **overfitted**, which leads to problems when we try to introduce our algorithm to new data.
