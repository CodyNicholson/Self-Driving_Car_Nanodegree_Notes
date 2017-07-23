# Resampling

We are given **N** particles, each which has 3 values, that each have their own weights (that are simple floats or continuous values). The sum of weights is **W**. We should normalize these weights to create a list of normalized weights that we call **alpha**. **alpha_1** would be the weight 1 divided by the normalizer **W**, and so on, all the way to **alpha_n**. The sum of all **alphas** is now 1, since it is normalized. What resampling does is it puts all these particles and normalized weights into a big bag and then it draws - with replacement - **N** new particles by picking each particle with probability **alpha**. In the end those particles have a high-normalized weight **alpha** will occur more frequently in the new set. 

![alt tag](imgs/resampling.PNG)
