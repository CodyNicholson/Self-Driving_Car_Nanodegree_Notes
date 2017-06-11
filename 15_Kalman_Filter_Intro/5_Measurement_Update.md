# Measurement Update

### Probability After Sense

![alt tag](imgs/probAfterSense.jpg)

As you can see in the image, there are to different states in the world that our car interprets in this example: red and green. Since the car senses red, the probability for our red cells increases and our probability for our green cells decreases since we multiply red call values by different numbers since we detected a red cell.

***

### Bayes Rule

The Bayes Rule is a product of our prior distribution with a measurement probability, which will be large if we are correct and small otherwise. We do this and assign it a so-called non-normalized probability, and then we compute the normalizer which is the sum of all the probabilities found in (P(Z|Xi)P(Xi))

```
X = grid cell
Z = measurement

P(Xi}Z) <- P(Z|Xi)P(Xi)

Normalizer = Summation(P(Xi|Z))

P(Xi|Z) <- (1/Normalizer) * P(Xi|Z)


Extra notes:
P(A|B) = P(B|A)*P(A) / P(B)
```

Cancer Test Example:

The probability that someone has cancer is: P(C) = 0.001

The probability that someone does not have cancer is: P(7C) = 0.999

The probability that the cancer test is positive for a person who has cancer is: P(Pos|C) = 0.8

The probability that the cancer test is positive for a person who does not have cancer is: P(Pos|7C) = 0.1

Now we need to use the Bayes Rule to calculate the probability that a person has cancer given that they tested positive: P(C|Pos) = ?

The answer is 0.0079, meaning that there is only a 0.79% chance that you have cancer if you are given a positive test result

To get this answer:

P(C|Pos) = P(C) * P(Pos|C), P(C|Pos) = 0.001 * 0.8 = 0.0079

The answer is 0.79%, meaning that the probability of getting a positive cancer test result given that you have cancer is 0.79%.

Then we can calculate the probability of getting a positive test result when you don't have cancer: P(7C|Pos) = ?

P(7c|Pos) = P(7C) * P(Pos|7C), P(7C|Pos) = 0.999 * 0.1 = 0.0999

The answer is 0.0999, meaning that you have a 9.99% chance of getting a positive cancer test result given that you don't have cancer.

We can then take the sum of these two probabilities we found, P(C|Pos) and P(7C|Pos), which would be 0.0008 + 0.0999 = 0.10007, and this is our normalization value. If we divide our P(C|Pos) by this normalization value we will get the probability, 0.79%, that we calculated earlier.
