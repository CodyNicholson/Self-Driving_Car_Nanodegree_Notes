# Derivation Outline

After learning the structure of the input data we will focus on two problems if we want to estimate the posterior directly

```
Posterior:

bel(x_t) = p(x_t|z_1:t, u_1:t, m)
```

1. The first problem is that the localizer must process on each cycle a lot of data (100s of GB per update)
2. The second problem is the amount of data increases over time

This will not work for a real-time localizer which should run at least 10 hertz in our vehicles

***

### Requirements For Fix

Change our localizer so it only needs to handle a few bytes on each update, and handles the same amount of data per update regardless of drive time
