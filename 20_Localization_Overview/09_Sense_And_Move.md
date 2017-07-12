# Sense & Move

At this point we know measurement updates and motion. We called these two routines **sense** and **move**. Localization is nothing else but the iteration of sense and move. There is initial belief that is tossed into this loop. If you sense first it senses, then moves, then repeats. Every time it moves it loses information as to where it is because movement is inaccurate. Every time it sense it gains information. This happens because after motion the probability distribution is a little bit flatter and a bit more spread out, and after sensing it's more focused.

There is a measure of information called the **entropy** that a distribution has and is expressed mathematically as: -(summation(p(x_i) * log_p(x_i)))

### Code

```python
#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print p         
```
