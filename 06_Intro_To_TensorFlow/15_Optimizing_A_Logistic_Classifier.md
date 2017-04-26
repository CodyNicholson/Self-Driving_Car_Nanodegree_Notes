# Optimizing A Logistic Classifier

Training Logistic Models using Gradient Descent is great since it optimizes the error measure. However, it is difficult to scale.

***

### Stochastic Gradient Descent

The problem with scaling gradient descent is that if it kes N operations to compute your loss (L=Summation i(D_i)), then it takes N times 3 operations to compute its gradient (-Alpha*Delta*Loss(w1,w2)). As we saw earlier, the Loss function is huge and it runs on every single element in your training set. That can be a lot of computing if your data set is big. We want to be able to train on lots of data because in practice, on real problems, you will always get more gains the more data you use. Since Gradient Descent is iterative, you have to do that for many steps. 

This is why we are going to cheat

Instead of computing loss using the loss function, we are going to compute an estimate of it. We are just going to calculate the loss of a very small random fraction of the training data, between 1 and 1000 training samples each time.

So we are going to take a very small sliver of the training data, compute the loss for that sample, compute the derivative for that sample, and pretend that that derivative is the right direction to use to do gradient descent.

It is not at all the right direction - and it might increase the real loss, not reduce it. We are going to compensate by doing this many many times taking very small steps each time. Each step is cheaper to compute, but we pay a price. We take many more small steps rather than one large step. **On balance though, we win by a lot**. This technique is called **Stochastic Gradient Descent** and it is at the core of Deep Learning since it scales well with both data and model size, and we want both big data and big models. Since SGD is fundamentally a pretty bad optimizer, that happens to be the only one that is fast enough, it comes with a lot of issues in practice. 
