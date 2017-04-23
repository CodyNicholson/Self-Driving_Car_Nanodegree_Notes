# Kernel Trick

To prevent us from having to create a bunch of new features to help our SVM classify the data, we can instead use the **kernel trick**.

There are functions that take low dimensional input space/feature space, and map it to a very high dimensional space (kernel functions). This makes features that were not linearly separable on a graph separable. Once you get the solution you are looking for from your high-dimensional input space, you can take that solution and change it back into its' original low input space.

Different kernel functions can be specified for the decision function of a SVM. Common kernels are provided by sklearn, but it is also possible to specify custom kernels. 

We used a linear kernel in the first quiz:

```python
from sklearn.svm import SVC
clf = SVC(kernel="linear")
```

This will make our decision boundary linear rather than jagged like rbf or curved like polynomial. The documentation for these kernel functions can be found [here](http://scikit-learn.org/stable/modules/svm.html#svm-kernels)
