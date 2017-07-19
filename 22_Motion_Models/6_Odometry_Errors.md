# Odometry Errors

When do you think using odometry from a wheel encoder will create large errors in your position estimates?

- On a slick, wet road
- On a road with lots of bumps

***

### Solution For Odometry Errors

On a slick, wet road the wheel encoder odometry will have large errors because the wheels will slip, causing them to travel less distance that expected. In addition, the wheels will also slide while braking.

On dry, paved roads the wheels will travel a distance very close to the expected circumference of the wheel

Roads with lots of bumps also create problems for odometry because we are assuming the car travels a straight distance in the direction of its heading. In reality, a bumpy road will cause the car to travel much of its distance up and down instead of a straight line.

On a road with lots of turns, wheel odometry works wheel because even though the heading of the car is changing, it's still moving the expected distance in the direction of its yaw. Despite the face that the distance vectors for this car are at different yaw angles, the sum of the absolute magnitude of all the vectors is the same as the expected distance traveled.
