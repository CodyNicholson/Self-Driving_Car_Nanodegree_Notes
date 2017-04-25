# Decision Tree Classifier Parameters

### min_smaple_split

the **min_sample_split** parameter tells the decision tree what the minimum number of samples is before it stops splitting up groups of data. The default value is 2. For example: If I have 100 samples and my first question in my decision tree splits that data into 60 and 40, those groups will continue to keep splitting until they reach a sample size less than 2.

By having a higher value for our min_sample split we can avoid unnatural shapes for our decision boundary since it will generalize the data more

![alt tag](minSampleSplit.jpg)

In the above picture you can see the difference between a graph with min_sample_split 2 and 50. Notice that the scatterplot with 50 is much cleaner since it has a higher value for min_sample_split.

#### min_sample_split Quiz

```python
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## DECISION TREE #################################

### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively


from sklearn import tree

clf50 = tree.DecisionTreeClassifier(min_samples_split = 50)
clf50.fit(features_train, labels_train)

clf2 = tree.DecisionTreeClassifier()
clf2.fit(features_train, labels_train)


pred50 = clf50.predict(features_test)
pred2  = clf2.predict(features_test)


from sklearn.metrics import accuracy_score

acc_min_samples_split_2  = accuracy_score(pred2, labels_test)
acc_min_samples_split_50 = accuracy_score(pred50, labels_test)

def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}
```

Output

```
{"message": "{'acc_min_samples_split_50': 0.912, 'acc_min_samples_split_2': 0.908}"}

```

![alt tag](minSampleSplit2.jpg)
