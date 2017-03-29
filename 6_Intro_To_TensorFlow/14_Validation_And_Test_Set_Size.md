#Validation & Test Set Size

Imagine that your validation set has just six examples with an accuracy of 66%

Now you tweak your model and your performance goes from 66% to 83% - but is it something you can trust? NO! This is only a change of a single example which could be just noise. 

The bigger your test set, the less noisy the accuracy measurement will be. A change that affects 30 examples in your validation set one way or the other is usually statistically significant and typically can be trusted.

***

###Example

If you have 3000 examples and you use the **Rule of '30'** described above, a change from 80% to 81% would be statistically significant whereas a change from 80.5% to 80% would not be

***

###Validation Set Size

Since we like to use the Rule of 30, we also like to keep our Validation Set Size above 30000 examples

This makes accuracy figures significant to the first decimal place (Changed >0.1% in accuracy) and gives you enough resolution to see small improvements.

If your classes are not well balanced (if some important classes are very rare), then this heuristic is no longer good. You will need much more data.
