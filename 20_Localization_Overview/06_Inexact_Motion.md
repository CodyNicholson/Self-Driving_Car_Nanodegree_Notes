# Inexact Motion

Given our five grid cell world, let's assume that a robot executes its action with high probability correctly - 80% - but it finds itself short of the intended action 10% of the time and also overshooting its target 10% of the time. Let's say our **U** value (how far our robot should move) is 2 (Since it is positive we will move to the right). According to our probabilities we defined there is an 80% chance we will move 2 spaces to the right, a 10% chance of moving one space to the right, and a 10% chance of moving 3 spaces to the right.

Mathematically this situation looks like this:

Current distribution: 0, 1, 0, 0, 0 (We know that the car is in the second cell)

U = 2

P(X_(i+2)|X_i) = 0.8

P(X_(i+1)|X_i) = 0.1

P(X_(i+3)|X_i) = 0.1

Output distribution: 0, 0, 0.1, 0.8, 0.1

***

Now we will solve for this situation:

Current distribution: 0, 0.5, 0, 0.5, 0

U = 2

P(X_(i+2)|X_i) = 0.8

P(X_(i+1)|X_i) = 0.1

P(X_(i+3)|X_i) = 0.1

Output distribution: 0.4, 0.05, 0.05, 0.4, 0.1

We go the above answer like this: Since there is a 50% chance that the car is starting in cell 2 that means that there is a 0.05 (0.1/2) chance that it will move to cell 3, a 0.4 (0.8/2) it will move to cell 4, and a 0.05 (0.1/2) chance it will move to cell 5. However, there is also a 50% chance the car will start in cell 4 meaning that there is a 0.05 (0.1/2) chance it will move to cell 5, a 0.4 (0.8/2) chance it will move to cell 1, and a 0.05 (0.1/2) chance it will move to cell 2. Since there are two probabilities in cell 5 we can add them together (0.05 + 0.05) to get 0.1

***

Localization is very important because we want to make our robots as accurate as possible when moving from one place to another

***

### Inexact Move Function

```python
#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
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
        s = pExact* p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

print move(p, 1)
```
