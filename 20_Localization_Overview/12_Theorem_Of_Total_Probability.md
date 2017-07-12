# Theorem Of Total Probability

The theorem of total probability relates to the motion step of our localization. Recall that we care about the probability of each individual grid cell in our distribution that can be represented as: **P(X_i)**. We ask: What is the chance of being in X_i after robot motion? To indicate the after and before we will add a time index: **P(X_i_t)**

**P(X_i_t)** = summation_j(X_j_(t-1) * P(X_i|X_j))
