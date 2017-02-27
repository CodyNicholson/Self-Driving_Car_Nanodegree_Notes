#Optimizing Weights

One of the things that goes wrong when you try and run gradient descent on a complex network with lots of data is that you get stuck in these local minima. Then you start to wonder if there is some other way that you can optimize these weights so they minimize error on the training set.

There are other types of advanced optimization methods that are useful to help minimize these errors.

This includes **Using Momentum** terms in the gradient, which basically just prevents us from getting stuck in a low dip in the data because the algorithm will use the "momentum" it gained from parsing through the higher data to push it over the next hill until it eventually finds the lowest point.

We can also use **Higher-Order Derivatives** to optimize things instead of just thinking about the way that individual weights change the error function to look at combinations of weights Hamiltonians, and what not.

There is also **Randomized Optimization** which can be applied to make things more robust.

Sometimes it also helps to not think so much about minimizing errors on the training set, we may actually want to have some kind of penalty for using a more complex structure. If we try to hard we may over-fit our data in a large tree or in regression. Things that cause a structure to be over complex are more nodes, layers, and large weights. 
