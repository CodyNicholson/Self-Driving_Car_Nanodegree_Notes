#Neural Network Vs Decision Tree

There are many differences between these two, but in practical terms, there are three main things to consider: speed, interpretability, and accuracy.

###Decision Trees

- Should be faster once trained (although both algorithms can train slowly depending on exact algorithm and the amount/dimensionality of the data). This is because a decision tree inherently "throws away" the input features that it doesn't find useful, whereas a neural net will use them all unless you do some feature selection as a pre-processing step.
- If it is important to understand what the model is doing, the trees are very interpretable.
- Only model functions which are axis-parallel splits of the data, which may not be the case.
- You probably want to be sure to [prune](http://en.wikipedia.org/wiki/Pruning_%28decision_trees%29) the tree to avoid over-fitting.

-

###Neural Nets

- Slower (both for training and classification), and less interpretable.
- If your data arrives in a stream, you can do incremental updates with stochastic gradient descent (unlike decision trees, which use inherently batch-learning algorithms).
- Can model more arbitrary functions (nonlinear interactions, etc.) and therefore might be more accurate, provided there is enough training data. But it can be prone to over-fitting as well.

-

You might want to try implementing both and running some experiments on your data to see which is better, and benchmark running times. Or, you could use something like the [Weka](http://www.cs.waikato.ac.nz/ml/weka/) GUI tooklit with a representative sample of your data to test drive both methods.

It may also be that using "bagging" or "boosting" algorithms with decision trees will improve accuracy while maintaining some simplicity and speed. But in short, if speed and interpretability are really important, then trees are probably where to start. Otherwise, it depends and you'll have some empirical exploration to do.
