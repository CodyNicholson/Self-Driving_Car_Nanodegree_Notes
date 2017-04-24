# Multiple Linear Questions

Decision trees allow you to ask multiple linear questions, one after the other. Each question would correspond to a new linear decision boundary in your scatterplot.

For example, if it needs to be both windy and sunny to go windsurfing, then you could make a decision tree that asks those two questions: Is it windy, and is it sunny. Our first question might be "Is it sunny". If this is true, then we check our next question: "Is it windy", otherwise we return false since it needs to be both windy and sunny to return true.

Here is the corresponding decision tree made for the above situation:

```
                               yes -> return true
                               /
            yes -> is it sunny?
            /                  \
Is it windy?                    no -> false
            \
            No -> return false
```
