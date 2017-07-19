## Bayes Filter Theory Summary

The Bayes localization filter, or Bayes filter is a general framework for recursive state estimation. Recursive means that we use the previous state to estimate the new state by using only current observations and controls, and not the whole history of data.

The motion model describes the prediction step of the filter. The observation model is the update step to estimate the new state probabilities. The current 1D localization, Kalman filters, and particle filters are realizations of the Bayes filter.
