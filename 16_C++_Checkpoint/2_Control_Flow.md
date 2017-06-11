# Control Flow

In this quiz, I want you to write a for loop. Your loop will live inside a function that will be passed an int, n, and a string, str. Your loop should print the str n times.

There's another twist here - you will not need to touch main.cpp this time. Instead, your code will be written inside the eponymous function in PrintString.cpp. Make note of the way that main.cpp #includes PrintString.h. You'll be #includeing files soon.

PrintString.cpp:

```c++
#include <iostream>
#include <string>
#include <PrintString.h>

using namespace std;

void PrintString(string str, int n)
{
    for (int i = 0; i < n; i++) {
        cout << str << endl;
    }
}
```

main.cpp:

```c++
#include <iostream>
#include <PrintString.h>

using namespace std;

int main()
{
    PrintString("This is a test.", 10);
}

```

PrintString.h:

```c++
/*
This header file defines the function signature for PrintString.
*/
#include <string>

void PrintString(std::string, int);

```
