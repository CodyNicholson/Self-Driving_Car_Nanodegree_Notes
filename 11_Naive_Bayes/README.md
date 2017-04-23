# Machine Learning & Stanley - Naive Bayes Classifier

Stanley was the self-driving car built by Sebastian Thrun and team at Stanford University that won the race through the desert against other universities' self-driving cars

A self-driving car is a giant supervised classification problem. **Supervised Classification** is a technique used to teach computers how to classify things by showing them tons of examples of those things.

In this section we create a program to tell the car what speed to go based on the terrain. To do this we will use a classifier called **Naive Bayes**.

***

### Naive Bayes Classifier Strengths & Weaknesses

Naive Bayes is good because:

- It is easy to implement
- It is very efficient to run this algorithm on large datasets (it scales)
- It is great for text categorization where it uses every word of an article as a feature (detect span, etc.)

Naive Bayes is bad at:

- It can't handle phrases that are composed of multiple words (If you search "Chicago Bulls" it will give you pictures of Chicago and pictures of Bulls, not basketball)
