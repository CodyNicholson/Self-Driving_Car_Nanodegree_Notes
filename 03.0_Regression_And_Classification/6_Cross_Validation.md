#Cross Validation

After you train your algorithm on your training set (with points and labels), you need to test it out on a different set af data called your testing set which does not have the labels. Your concept will give the data in your testing set labels and then you can check to see if it was right.

**The goal is always to generalize**, we don't test on the training set because we want our program to be ready for real-world random data. If we don't generalize our program won't be able to guess correctly in the real world with real data. 

All data needs to be independant and identically distributed, all the data that we have collected is all coming from the same source. All draw from same distribution. 

Test and training set data represent the real world data our program will need to be ready for. 

***

We need to use a model that is complex enough to model the structure that's in the data that we're training on, but not so complex that it's matching so well that is doesn't work on the test set. However, we don't have the test because we can't do too much teaching from the test. We need to actually learn the true structure that is going to need to be generalized. How can we pick a model that is complex enough to model the data while making sure that it hasn't started to kind of diverge in terms of how it's going to be applied to the test set. 

Since we don't have access to the test set, we can use a partition of the training set to **Cross Validate** our program. The partitions of a set are called folds. If we divide our training set into four folds, we can train on the first three and then use the fourth fold as a testing set to see how we did. Then we can average the results together to see how well we did. 
