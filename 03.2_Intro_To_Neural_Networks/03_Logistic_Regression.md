# Logistic Regression

In **Logistic Regression** we are not trying to determine a point based on the location of other points like Linear Regression, instead we are trying to classify points based on their locations on a graph. We do this by drawing lines on our graph to separate the points into groups.

The line that we draw to separate data points into classes is called our **Model**. Every time we get a new input, we use our model to classify that new input and label it accordingly. 

To create our model we start by drawing a random line through the data. Then we check how many errors our line makes - where an error is a incorrectly classified data point. Then after we check have checked our errors, we will keep adjusting the line until we have the smallest amount of errors using Gradient Descent. To use the Gradient Descent properly we do not want to minimize the errors, we want to use the **Log-Loss Function**.

We assign values to all of our points. Small values for correctly classified points and large values for incorrectly classified points. To find our error we add up all the values of the points in our graph. Then we keep changing the line until we find the position that will minimize the error value. 
