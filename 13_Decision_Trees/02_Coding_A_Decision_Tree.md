# Coding A Decision Tree

studentMain.py

```python
import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)


#### grader code, do not modify below this line
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
```

classifyDT.py

```python
def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)
    
    return clf
```

***

Creating and training a decision tree classifier is the same syntax for creating the classifiers we worked with previously

When you plot this, long unnatural slices indicate overfitting of the data.


***

### Evaluating A Decision Tree

```python
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## DECISION TREE #################################

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)


### be sure to compute the accuracy on the test set

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)
    
def submitAccuracies():
  return {"acc":round(acc,3)}
```
