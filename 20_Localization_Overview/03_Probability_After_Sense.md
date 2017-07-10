# Probability After Sense

![alt tag](imgs/probabilityAfterSense.png)

We start in our five-cell world with a uniform distribution - so our car has a 20% chance of being at any one of the five cells. As seen above, three of the cells are green and two are red.

After the car senses where it is for the first time, it discovers that it is in a red cell. Since we are at a red cell we need to update our probability distribution to reflect this so we multiply all of the red cell probabilities by 0.6 (pHit) and all of the green cell probabilities by 0.2 (pMiss) which gives us our second distribution in the picture above. The problem is that these probabilities only add to 0.36 - not 1.

To fix this we divide the each of the probability values in our distribution by the sum of these values: 0.36. This results in a new distribution that does sum to one and reflects the probability of our car being at each cell.

This is called our **Posterior Distribution**

***

### Code

```python
#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.

p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

p[0] *= pMiss
p[1] *= pHit
p[2] *= pHit
p[3] *= pMiss
p[4] *= pMiss

print p

#Modify the program to find and print the sum of all 
#the entries in the list p.

print sum(p)
```
