# How Much Data

How much data is in **z_t:1**?

This is important so we can consider what the performance consequences would be. So let's pretend that each observation vector contains 100,000 data points, of observations. Each of those observations may have five data points, which take four bytes each. If we have been driving a car for six hours with our sensor updating at 10 Hertz, how much data is contained in this set 1 to t?

- LIDAR sends 100,000 data points per observation
- LIDAR refreshes 10 times per seconds (10 Hertz)
- Each observations contains 5 pieces of data
- Each piece of data requires 4 bytes
- The car has driven for 6 hours

6 hrs * 3,600 seconds * 10 cycles per second * 100,000 observations per cycle * 5 data points per observation * 4 bytes per data point = 432

Answer: **432 GB**

This is a good sense of the quantity of the data that a real car would use if its update step took into account all historical observations. Later we will explore how to get around this limitation.
