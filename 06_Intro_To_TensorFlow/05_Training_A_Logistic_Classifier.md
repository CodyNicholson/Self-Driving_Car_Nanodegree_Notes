# Training A Logistic Classifier

#### WX + b = y

A **Logistic Classifier** is a type of *linear classifier*. It takes the inputs (maybe the pixels of an image) and applies a linear function to those inputs to get its prediction

A linear function is just a giant matrix multiply

It takes all the inputs as a big vector that we denote *X* and multiplies them with a matrix to generate predictions - one prediction per output class

We will denote our weights as *W* and our biased term *b*, and we will denote our vector of outputs as *y*

-

The weights of the matrix and the bias is where the machine learning comes in. We are going to train that model - Which means that we are going to try to find values for the weights and bias, which are good at performing those predictions

We use those scores to perform the classification

Each image can only have one possible label, so we are going to turn those scores into probabilities so that we can select the single label with the highest probability (closest to one)

We will use a **SoftMax Function** to turn our scores into probabilities:

#### S(y_i) = (e^y_i)/(Summation j(e^y_j))
