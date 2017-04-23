# Support Vectors Machines (SVM)

SVM's are able to draw a line between our data called a **hyperplane** that maximizes the distance between the nearest point relative to both classes. This is very useful because if we can separate the data well it makes it very easy for our classifiers to make decisions.

***

### SVM Strengths & Weaknesses

Strengths:

- They work really well in complicated domains where there is a clear margin of separation

Weaknesses:

- They don't perform well on large datasets because the training time is cubic in the size of the dataset
- They also don't work well with lots of noise, so when the classes are overlapping you have to count independent evidence (Naive Bayes would be better here)

Make sure to think about the dataset and the features that you have available when choosing which classifier to use
