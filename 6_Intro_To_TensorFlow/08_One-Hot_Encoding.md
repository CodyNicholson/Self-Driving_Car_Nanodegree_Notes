#One-Hot Coding

Our Softmax algorithm needs a way to represent our labels (classes) mathematically. This can be done using **One-Hot Encoding**.

We can encode the correct class with the value 1, and all the incorrect classes with the value 0. For example, if your algorithm is trying to classify an image as the letter "a" then it should have a class for every character in the alphabet. The "a" class will be assigned the value 1, and all the other letters in the alphabet (other classes) will have the value of 0.

***

###Examples:

Given a picture of the letter "a" the one-hot encoded classes would be:

a = 1

b = 0

c = 0

...

-

Given a picture of the letter "c" the one-hot encoded classes would be:

a = 0

b = 0

c = 1

...
