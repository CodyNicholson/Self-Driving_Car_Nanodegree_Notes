# The Chain Rule

#### x => multiply, add => RELU => multiply, add, => y => S(Y) => (output vector)

One reason to build this network by stacking simple operations (like multiplications, sums, and RELUs) on top of each other is that it makes the math very simple

Simple enough that a deep learning framework can manage it for you

The key mathematical insight is **the chain rule**

***

If you have two functions that get composed, that is, one is applied to the other, then the chain rule tells you that you can compute the derivatives of that function simply by taking the product of the derivatives of the components

> Derivative [g(f(x))]' = Product g'(f(x)) * f'(x)

***

As long as you know how to write the derivatives of your individual functions, there is a simple graphical way to combine them together and compute the derivative for the whole function

```
Function: x => f() => g => y

                                y'
                                ^
                                |
Derivative: x => f() => g'() => * <= f'() <= x
```

Efficient data pipeline

Lots of data reuse
