# Bayes Rule

Bayes Rule is the most fundamental consideration in probabilistic inference

Suppose **X** is a grad cell and **Z** is my measurement. Then the measurement update seeks to calculate a belief over my location after seeing the measurement:

**P(X_i|Z)** = (P(Z|X_i) * P(X_i)) / P(Z)

It takes the prior distribution **P(X_i)** and multiplies in the chances of seeing a red or green tile for every possible location (Measurement probability): **P(Z|X_i)**. The measurement probability is large if the color is correct, and small otherwise. This outputs the non-normalized posterior distribution we had before: **P(X_i|Z)**.

**P(Z)** is the sum over all **i** of the product of **P(Z|X_i) * P(X_i)**

Bayes Rule is the product of our prior distribution with a measurement probability (large if correct color, small otherwise). We do this and assign it to a non-normalized probability. Then we compute the normalizer, called **alpha**, which is the sum of all the **P(X_i|Z)**. We can then normalize this by multiplying this by (1/alpha): **(1/alpha) * P(X_i|Z)**

***

### Cancer Test Quiz For Bayes Rule

Probability that someone has cancer:

P(C) = 0.001

Probability that someone does not have cancer:

P(7C) = 0.999

Probability that the cancer test is positive if you do have cancer:

P(POS|C) = 0.8

Probability that cancer test is positive and you don't have caner:

P(POS|7C) = 0.1

##### What is the probability that a person has cancer given that they receive a positive result?

**0.0079** - since: P(C) * P(POS|C) = 0.0008 (Probability of a positive result in cancer state), and the probability of a non-cancerous person being given a positive cancer test is: P(7C) * P(POS|7C) = 0.0999

Our normalizer (alpha) is the sum of those two values: **0.1007**

Then dividing 0.0008/0.1007 gives us: **0.1007**
