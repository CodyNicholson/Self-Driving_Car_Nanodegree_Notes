# Localization

Localization involves a robot that is lost in space and has no clue where it is. In our case, this robot is a self-driving car and it is lost on some road. The traditional way to solve this localization problem is to use satellites that emit a signal that the car can perceive known as GPS. The problem with GPS is that it is not accurate enough for our purposes. 

#### Our question becomes: How can we learn where we are with 10cm of accuracy?

We record images of the road surface and then use techniques to find out exactly where the robot is. It can do this within a few centimeters of accuracy and can thus stay in its lane even if the lane markers are missing.
