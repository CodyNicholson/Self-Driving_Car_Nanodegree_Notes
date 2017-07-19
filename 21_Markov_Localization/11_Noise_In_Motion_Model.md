# Noise In Motion Model

Assume you have a 1D space between 0 and 30 meters. At the very beginning the robot or the car has no clue where it is. So our initial belief would be the uniform distribution, which means maximum confusion. Now we assume the car knows it is parked closely to a tree. Then, the initial belief graph would have spikes next to every tree in our 1D world.

How does the belief look after we look 10 meters to the right with low noise, and with high noise?

If we move with no noise - which means the transition model is certain - then we just shift the belief 10 meters to the right without any loss of information. No noise does not mean we get better precision.

If we move with low noise, the belief is spread out, but we can still see short peaks

If we move with high noise, the belief is spread out even more so that the peaks are no longer defined at all - almost uniform
