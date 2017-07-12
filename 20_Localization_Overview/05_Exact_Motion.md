# Exact Motion

Suppose we have a distribution over a five-cell world like before with probabilities:

| 1/9 | 1/3 | 1/3 | 1/9 | 1/9 |

Lets say that even though the robot does not know where it is, it moves to the right. Assume that this world is cyclic meaning that moving right from the last cell will take you to the left side of the first cell. The probabilities would then shift to the right with the robot:

| 1/9 | 1/9 | 1/3 | 1/3 | 1/9 |

In the case of exact motion, we have a perfect robot. We just shift the probabilities by the actual robot motion (right) like we did above. This is a degenerate case, but it is a good one to program first.

***

### Move Function Code

We can define a function move() with an input distribution **p** and a motion number **U**, where **U** is the number of grid cells that the robot is moving to the right or to the left. 

```python
#Program a function that returns a new distribution 
#q, shifted to the right by U units. If U=0, q should 
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)])
    return q

print move(p, 1)
```
