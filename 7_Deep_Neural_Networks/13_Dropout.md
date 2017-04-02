# Dropout

Another important technique for regularization is called **Dropout**. How it works is: imagine you have one layer that connects to another layer. The values that go from one layer to the next are called activations. Now take those activations, and randomly, for every example you train your network on, set half of them to zero. You basically take half of the data thats flowing through your network and you get rid of it. 

Why do we do this?

Using Dropout, your network can never rely on any given activation to be present because they might be squashed at any given moment. So it is forced to learn a redundant representation for everything to make sure that at least some of the information remains. One activation might get removed, but there is always one or more that do the same job and don't get removed. So everything remains in the end.

Forcing your network to learn redundant representations might sound very inefficient, but in practice it makes things more robust and prevents overfitting. It also makes your network act as if taking the consensus over an ensemble of networks, which is always a good way to improve performance.

If Dropout does not work for your model, you should probably be using a bigger network

***

### Dropout Part 2 - Render

When you evaluate the network that has been trained with dropout, you no longer want this randomness. You want something deterministic, so you should take the consensus over these redundant models. You get the consensus by averaging the activations. You want Y_e to be the average of Y_t's that you got during training. 

A trick to do this is to not only use the zero out so the activations that you dropout during training, but you also scale the remaining activations by a factor of 2. This way, when it comes time to average them  during evaluation, you just remove these dropouts and scaling operations from your neural net. The result is an average of these activations that is properly scaled.
