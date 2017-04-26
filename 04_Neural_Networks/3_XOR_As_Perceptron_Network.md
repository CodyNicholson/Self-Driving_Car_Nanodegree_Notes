# XOR As Perceptron Network

XOR will return 0 if both the inputs are the same and true if both the inputs are different. On a graph you cannot portray this relationship with a single line, so we need to use a network of Perceptrons to accomplish this task.

To solve this we need to set three weights: The first for x1, the second for x2, and the third for the case where x1 and x2 are the same.

w1 = 1

w2 = 1

w3 = -2

Theta = 1

Using the above values, if x1 is 0 and x2 is 1 then (0*1 + 1*1) gives us 1 which is greater than or equal to our threshold of 1

If x1 is 1 and x2 is 1 then we calculate (1*1 + 1*1) give us 2 which would activate our neuron, but we then use our "And" weight to which multiples our 2 by -2 and gives us -4, which does not activate our neuron.

If x1 and x2 are 0 then ((0*1 + 0*1)*-2) equals 0. Notice we multiplied by -2 since the and was true in this case.
