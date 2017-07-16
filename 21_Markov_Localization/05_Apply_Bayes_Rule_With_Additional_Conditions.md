# Apply Bayes Rule With Additional Conditions

```
Posterior:

bel(x_t) = p(x_t|z_1:t, u_1:t, m)
```

We know that the **z** in the above equation represents our observation vector, and it can be a lot of data, and we do not want to carry the whole observation history to estimate the state beliefs. The idea is now that we manipulate the posterior in such a way that we get a recursive state estimator. We have to show that the current belief can be expressed by the belief one step earlier, and then update the current belied only with new observation information.

We call this estimator the Bayes localization filter, or **Markov localization**. This will allow us to avoid having to carry around all historical observation and motion data. To achieve this recursive structure we have to apply probabilistic rules and laws like the Bayes rule or the law of total probability. We will also learn about the Markov assumption. This involves making meaningful assumptions about the dependencies between uncertain values.

Our goal is to find the posterior in a recursive way. This means that we want to find the value of **bel(x_t)**

The first thing we do is split the observation vector into the current observations and our previous information. This is important to achieve the recursive structure. REmember:

```
Observation list:

z_1:t = {z_t, ..., z_1}

Vector of Distances:

z_t = [z_t_1, ..., z_t_k]
```

Now we apply Bayes rule:

```
Bayes Rule:

p(x_t|z_t, z_1:t, m) = ??
```

Bayes rule is the most fundamental consideration in probabilistic inference

```
p(a|b) = (p(b|a) * p(a)) / p(b)

p(a|b) is posterior
p(b|a) is likelihood
p(a) is prior
p(b) is normalizing constant
```

The tricky part here is that you have more than one variable on the right side which means that you have to apply Bayes rule

***

### How Would We Apply Bayes Rule For The Localization Posterior?

Assume that state **x_t** is **a** and the observation vector at **t** is **b**

