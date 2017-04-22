# Statistical Invariance

Imagine you want to train a network to recognize that there is a cat in the image. It doesn't matter where the cat is in the image, it's still an image with a cat in it. If your network has to learn about cats in the left corner and cats in the right corner independently, that is a lot of work that it has to do.

We need to tell the network explicitly that objects and images are largely the same whether they're in the left or right corner, or anywhere else in the picture. This is called **Translation Invariance**.

***

### Weight Sharing

Imagine you have a long text that talks about cats. The meaning of "cat" does not change much depending on the location of the word. So if you train a network on text, you want the part of the network that learns what a "cat" is to be reused every time you see the word, instead of having to relearn it every time. 

The way you achieve this is by using **Weight Sharing**. When you know that two inputs contain the same kind of information, then you share the weights and train the weights jointly for those inputs. 

**Statistical Invariants**, things that don't change on average across time or space, are everywhere. For images, the idea of **Weight Sharing** will get us to study *Convolutional Neural Networks*. For text and sequences in general, it will lead us to embeddings and *Recurrent Neural Networks*.
