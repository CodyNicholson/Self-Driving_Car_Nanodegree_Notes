# Supervised Learning

There are two types of **Supervised Learning**: *Classification* and *Regression*

***

**Classification** is the process of taking some kind of input and mapping it to some kind of discrete label

**Regression** is all about continuous values. For example, given some point you can use regression to map it to some value based on the location of other similar points on some graph.

***

The difference between classification and regression is the difference between mapping from some input some small number of discrete values (Classification), and mapping from some input space to some real number (Regression).

***

### Classification Or Regression:

**Input**: Credit history
**Output**: Should I lend money to this person (T/F)?
**Answer**: Classification
**Explain**: Output is binary, therefore we classify it

**Input**: Image Of Person
**Output**: Are they in school, undergrad college, graduate college?
**Answer**: Classification
**Explain**: Output is one of three categories (or discrete sets), therefore classification

**Input**: Image of person
**Output**: Age
**Answer**: Regression, but you could do it with Classification too, but not as well as with Regression
**Explain**: Since Age is continuous regression would be best, but you could also make a discrete set of all ages and do classification too. It would not preform as well, though.
