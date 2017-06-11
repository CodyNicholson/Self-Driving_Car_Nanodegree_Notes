# Functions

In this quiz, I want you to write a function called factorial that returns an int. A factorial is a mathematical operation designated by a ! operator and returns the product of a number and every whole number between it and 0. For example:

4!=4⋅3⋅2⋅1=24

You'll write your code within Factorial.cpp. Good luck!

Factorial.cpp:

```c++
#include <Factorial.h>

int Factorial(int n)
{
    int result = 1;

    for (int i = n; i > 0; i--) {
        result *= i;
    }

    return result;
}
```

Factorial.h:

```c++
/*
No need to change this file. This simply declares that Factorial returns an int
and takes an int as the sole argument.
*/
int Factorial(int n);
```

main.cpp:

```c++
#include <iostream>
#include <Factorial.h>

int main()
{
    // feel free to change this test case!
    int value = Factorial(6);
    std::cout << "6! should equal 720. Your Factorial method returned:" << std::endl;
    std::cout << value << std::endl;
}

```

I took advantage of the *= operator to multiply result by a lower int and then reset itself to the new value simultaneously.
