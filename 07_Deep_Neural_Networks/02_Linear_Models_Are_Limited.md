# Linear Models Are Limited

#### y = x1 + x2

The above equation is something you could make a linear model for since the inputs interact in an additive way. The model can represent this well as a matrix multiply. 

#### y = x1 * x2

This above equation's outcome depends on the product of the two inputs. Because of this it will not be efficient to model this with a linear model. 

***

Big matrix multiplies are what GPUs were designed for

***

Numerically, linear operations are very stable. We can show mathematically that small changes in the input can never yield big changes in the output:

y = w * x -> Delta y ~ |W| Delta x

The derivatives are nice too because the derivative of a linear function is constant

We want to keep our parameters inside big linear functions, but we also want the entire model to be nonlinear
