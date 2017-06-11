# stdout

Let's start with an easy one. In this quiz, I'm giving you a main function. All I want you to do is write no more steering wheels to stdout.

Just as a reminder, anything written to stdout will appear below the code editor after you test or submit your code.

```c++
#include <iostream>

int main()
{
    std::cout << "no more steering wheels" << std::endl;
    return 0;
}
```

std refers to namespace std and the << operator passes sequences of characters to stdout. In fact, two sequences of characters get passed to stdout: "no more steering wheels" and std::endl, a newline character (std::endl also flushes the buffer).

It's worth noting that "no more steering wheels" is not a string like a Python string, rather it's a char [] - a sequence of characters.
