# Naive Bayes

Using a library called **sklearn** we can implement the *Naive Bayes* classifier to create a decision surface to classify the data points in our scatter plot

##### Gaussian Naive Bayes

```python
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]) # features
>>> Y = np.array([1, 1, 1, 2, 2, 2])  # Labels
>>> from sklearn.naive_bayes import GaussianNB  # Import Naive Bayes
>>> clf = GaussianNB()  # Create a classifier
>>> clf.fit(X, Y)       # Fit (train) the data using the training data
GaussianNB(priors=None)
>>> print(clf.predict([[-0.8, -1]])) # Predict what this data point will be based on the others
[1]  # It predicted that the above point would be in class 1
```

##### Quiz

classify.py:

```python
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    print(pred)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    return accuracy
```

student code:

```python
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy
```

output:

```
[ 0.  1.  1.  0.  1.  1.  1.  0.  1.  1.  1.  1.  1.  0.  0.  1.  0.  1.
  0.  1.  1.  1.  0.  1.  1.  1.  1.  1.  1.  0.  1.  1.  1.  1.  0.  1.
  1.  0.  1.  0.  1.  0.  1.  1.  1.  1.  1.  1.  0.  1.  0.  1.  0.  1.
  1.  0.  1.  0.  1.  1.  1.  1.  1.  1.  0.  1.  1.  0.  1.  1.  1.  1.
  1.  1.  1.  0.  1.  0.  1.  1.  1.  1.  1.  1.  1.  1.  0.  0.  0.  1.
  0.  1.  1.  1.  1.  1.  1.  0.  1.  1.  1.  0.  0.  1.  1.  1.  1.  0.
  1.  1.  1.  1.  1.  1.  0.  1.  0.  0.  0.  0.  1.  1.  0.  1.  1.  1.
  1.  1.  0.  0.  0.  0.  1.  1.  1.  1.  1.  0.  1.  1.  1.  0.  1.  1.
  0.  1.  1.  0.  1.  0.  1.  1.  1.  0.  0.  1.  1.  1.  0.  1.  1.  1.
  0.  1.  1.  0.  1.  1.  1.  1.  1.  1.  1.  1.  0.  0.  1.  1.  1.  1.
  1.  1.  0.  0.  0.  1.  1.  1.  1.  0.  1.  1.  1.  1.  1.  0.  1.  0.
  1.  1.  1.  1.  1.  1.  1.  1.  0.  1.  1.  1.  1.  0.  1.  1.  1.  0.
  0.  1.  0.  1.  0.  1.  1.  1.  1.  0.  1.  1.  0.  0.  0.  1.  0.  1.
  0.  1.  1.  0.  1.  1.  0.  0.  0.  1.  1.  0.  1.  1.  1.  1.]
{"accuracy": "0.884"}
```
