# Initialization

![alt tag](imgs/flowChart.PNG)

The very first thing we need to do to implement a particle filter is initialize all your particles. You'll have to decide how many particles you want to use. This parameter is mostly decided empirically, but theoretically the particle filter will exactly represent the Bayesian posterior distribution as a number of particles approaches infinity. If you have too few particles, you will not have enough to cover all of the high likelihood positions, so you might miss the correct position. For instance, if each cell in a 4x4 grid is equally likely to be the car's position, and you only have 3 particles, you wouldn't have enough particles right now to represent this.

Having too many particles will slow down your filter, and prevent it from localizing a self-driving car in real time. There are two main ways you can initialize you particles:

1. The first is to sample uniformly across the state space. For instance, you could divide the state space into a grid, and put 1 particle in each cell. However, this approach is not very practical if the state space is too large, such as in the case of a self-driving car, where the state space spans the entire land surface of the earth.
2. The second approach for initialization is to sample around some kind of initial estimate. For a self-driving car, this initial estimate can come from a GPS. We cannot rely on a GPS alone because of its low accuracy and reduced availability in certain environments. However, it can be very useful to provide initial rough estimates of your location.

In the project we will initialize a particle filter by sampling from a Gaussian distribution, taking into account sensor noise around the initial GPS position estimate and the initial heading estimate

```c++
/*
 * print_samples_sol.cpp
 * 
 * Print out to the terminal 3 samples from a normal distribution with
 * mean equal to the GPS position and IMU heading measurements and
 * standard deviation of 2 m for the x and y position and 0.05 radians
 * for the heading of the car. 
 *
 * Author: Tiffany Huang
 */

#include <random> // Need this for sampling from distributions
#include <iostream>

using namespace std;

// @param gps_x     GPS provided x position
// @param gps_y     GPS provided y position
// @param psi       GPS provided yaw
void printSamples(double gps_x, double gps_y, double psi) {
    default_random_engine gen;
    double std_x, std_y, std_psi; // Standard deviations for x, y, and psi

    // Set standard deviations for x, y, and psi
     std_x = 2;
     std_y = 2;
     std_psi = 0.05;
     

    // This line creates a normal (Gaussian) distribution for x
    normal_distribution<double> dist_x(gps_x, std_x);
    
    // Create normal distributions for y and psi
    normal_distribution<double> dist_y(gps_y, std_y);
    normal_distribution<double> dist_psi(psi, std_psi);

    
    for (int i = 0; i < 3; ++i) {
        double sample_x, sample_y, sample_psi;
        
        // Sample  and from these normal distributions like this: 
        //   sample_x = dist_x(gen);
        //   where "gen" is the random engine initialized earlier.
        
         sample_x = dist_x(gen);
         sample_y = dist_y(gen);
         sample_psi = dist_psi(gen);     
         
         // Print your samples to the terminal.
         cout << "Sample " << i + 1 << " " << sample_x << " " << sample_y << " " << sample_psi << endl;
    }

}

int main() {
    
    // Set GPS provided state of the car.
    double gps_x = 4983;
    double gps_y = 5029;
    double psi = 1.201;
    
    // Sample from the GPS provided position.
    printSamples(gps_x, gps_y, psi);
    
    return 0;
}
```
