# Localization Overview

In this lesson we learned about localization, we wrote an algorithm that implements what is called **Markov Localization**, we learned about probabilities, Bayes rule, and total probability

***

Localization maintains a function over all possible places where a road might be, where each cell has an associated probability value

The measurement update function, or "sense", is nothing else but a product in which we take those probability values and multiply them up or down depending on the exact measurement. Since the product might violate the fact that probabilities add up to 1, there was a product followed by normalization.

Motion was a convolution. This means that for each possible location after the motion we reverse engineered the situation and guessed where the world might have come from and then collected, we added the corresponding probabilities.

Something as simple as multiplication and addition solves all of localization and is the foundation for autonomous driving
