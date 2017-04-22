#Measuring Performance

A classifier will always try to compare new data to data it has seen before in the training set. When it sees new data originally, it will have no idea what to do. This is why we need to help our classifier generalize more so it can handle new data well. 

To solve this problem we hide a small portion of our test set from the classifier. The classifier will never see this portion of the tst set until you think your classifier is ready for it. **When you finally do test on your hidden portion of the data you can use that result to measure your real performance**. You can use your Validation set (The set of your training data that you did not hide) to measure your actual error.

The bigger your validation set the more precise your numbers will be.
