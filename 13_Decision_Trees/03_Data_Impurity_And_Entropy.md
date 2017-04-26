# Data Impurity & Entropy

**Entropy** controls how a decision tree decides where to split the data. It is a measure of impurity in a bunch of examples. It is the measure of the impurity in a bunch of examples.

If all examples in a subset are of the same class, then entropy = 0. If the examples are evenly split between classes, then entropy = 1 (It's highest possible value).

The **Purity** of a subset of your scatterplot is decided by how much of a single class your subset contains. If all the data points in your subset are of the same class, then your subset is 100% pure - or 0% impurity.

When building a decision tree, you are trying to find variables and split points along those variables that is going to make subsets that are as pure as possible. By repeating that process recursively, that is how the decision tree actually makes its decisions.

***

### Entropy Formula

```
Entropy = Summation i(-P_i(log_2(P_i)))
```

**P_i** is the fraction of examples that are in a given class, class i. Then you sum over all the classes that are available.

Some sources use other bases for the logarithm (for example, they might use log base 10 or the natural log, with a base of approx. 2.72)--those details can change the maximal value of entropy that you can get. In our case, where there are 2 classes, the log base 2 formula that we use will have a maximal value of 1.

In practice, when you use a decision tree, you will rarely have to deal with the details of the log base--the important takeaway here is that lower entropy points toward more organized data, and that a decision tree uses that as a way how to classify events.

***

### Entropy Calculation Example

| grade     | bumpiness | speed limit | speed |
|:---------:|:---------:|:-----------:|:-----:|
| steep     | bumpy     | yes         | slow  |
| steep     | smooth    | yes         | fast  |
| flat      | bumpy     | no          | fast  |
| steep     | smooth    | no          | fast  |

Above there are four rows of data. We want to calculate the entropy for the class "speed" that has a value of "fast" or "slow". Of the four rows, 3 of them have a "speed" value of "slow", and 1 row has a "speed" value of "fast". 

The first step is to calculate the P_i of the values "slow" and "fast" of the class "speed". P_Slow = (Number of rows with "slow") / (Total number of rows). This equates to: P_Slow = 3/4 = (0.75). Thus, the P_Fast = 1/4 = (0.25). Now that we have these two values we can do our calculation:

Calculation:

```python
import math

print((-0.75 * math.log(0.75, 2)) - (0.25 * math.log(0.25, 2)))
```

Output Entropy:

```
0.8112781244591328
```

The most "impure" entropy is 1.0. The most "pure" - or lowest entropy - is 0.0 where all data points in a subset belong to the same class. That being said, an entropy of 0.81 is very impure, but not the most impure.
