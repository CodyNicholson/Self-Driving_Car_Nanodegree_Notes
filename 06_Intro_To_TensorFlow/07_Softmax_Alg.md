# Softmax Algorithm

The next step is to assign a probability to each label, which you can then use to classify the data. Use the softmax function to turn your logits into probabilities.

S(y_i) = (e^y_i)/(Summation j(e^y_i))

We can do this by using the formula above, which uses the input of y values and the mathematical constant "e" which is approximately equal to 2.718. By taking "e" to the power of any real value we always get back a positive value, this then helps us scale when having negative y values. The summation symbol on the bottom of the divisor indicates that we add together all the e^(input y value) elements in order to get our calculated probability outputs.

***

Softmax function example:

```python
def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)
    
    # TODO: Calculate the softmax of the logits
    softmax = tf.nn.softmax(logits)
    
    with tf.Session() as sess:
        # TODO: Feed in the logit data
        output = sess.run(softmax, feed_dict={logits: logit_data})

    return output
```

Output:

```
[ 0.65900117  0.24243298  0.09856589]
```

***

### Important Note

If you increase the size of the y that you pass through your Softmax function (S(y*10)) then your algorithm will make your classifier very confident about its predictions.

If you decrease the y that you pass through your Softmax function (S(y/10)) then your algorithm will become much less confident about its predications.

You can use this trick at different times in your system to get the best end result. For example, maybe you would make it so that your algorithm was not confident to start, but as you run the algorithm more and more you manipulate the y to make it more confident later on.
