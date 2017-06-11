# Class Basics

In this challenge, I want to flip the tables a bit. In the previous quizzes, I've been giving you header files and asking you to implement methods from them. In this quiz, I'm going to give you a .cpp file and ask you to write the corresponding header file.

In Car.cpp, you'll find the implementation of a simple Car class. This is a very unreliable car that has a 50/50 chance of being broken after every drive.

I want you to examine Car.cpp and write the corresponding header file, Car.h. The code you'll find below won't compile without a working header file. Check out the compiler errors and make it work!

Car.h:

```c++
class Car {
    private:
        bool in_working_condition_;

    public:
        Car();
        void wearAndTear();
        bool drive();
        void fix();
};
```

Car.cpp:

```c++
/*
This is how the car works. No need to make any changes here.
*/
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <Car.h>

using namespace std;

/**
 * Constructor.
 */
Car::Car()
{
    // initialize random seed for wearAndTear
    srand(time(NULL));
    // start off in working condition
    in_working_condition_ = true;
}

/**
 * Determine whether or not the car is still drivable after some wear and tear.
 */
void Car::wearAndTear()
{
    // 50% chance that the car is still working after wear and tear
    int condition = rand() % 10;
    condition >= 5 ? in_working_condition_ = true : in_working_condition_ = false;
}

/**
 * Try to drive the car.
 */
bool Car::drive()
{
    bool didDrive = false;

    if (in_working_condition_) {
        cout << "Driving!" << endl;
        wearAndTear();
        didDrive = true;
    } else {
        cout << "Broken down. Please fix." << endl;
        didDrive = false;
    }

    return didDrive;
}

/**
 * Fix the car.
 */
void Car::fix()
{
    in_working_condition_ = true;
    cout << "Fixed!" << endl;
}

```

main.cpp:

```c++
/*
Here is a test of your code. Feel free to play with it but there's
no need to edit this file. Remember, you're only trying to make your code
compile.
*/
#include <Car.h>

int main()
{
    Car car;
    
    // try to drive 10 times
    for (int i = 0; i < 10; i++) {
        bool didDrive = car.drive();
        if (!didDrive) {
            // car is broken! must fix it
            car.fix();
        }
    }
    
    return 0;
}

```

The Car class is pretty straightforward. The trickiest part, I found, was making sure that the constructor was defined.

Note, the trailing _ on in_working_condition_ is common tactic for designating private properties in C++
