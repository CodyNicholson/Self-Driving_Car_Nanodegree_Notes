# Using The Robot Class

```python

```

The main class is a class called Robot. This robot lives in a 2D world of size 100 meters x 100 meters. It can see 4 different landmarks that are located at the coordinates stored in the **landmarks** object.

To make a robot all we have to do is call the function **robot()** and assign it to a variable **myrobot**. We can set a position for our robot using the **set()** function defined. The three value we pass the **set()** function are the x-coordinate, the y-coordinate, and the heading  in radians. We can print the resulting robot like this:

```python
myrobot = robot()
myrobot.set(10.0, 10.0, 0.0)
print myrobot
```

output:

```
[x=10.0 y=10.0 heading=0,0]
```
