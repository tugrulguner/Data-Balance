Here I am adding a very simple code to automatically balance target dataset through down and upsampling it.

This balance function (balance(data, target, sampling_amount)) takes training data and target column name as DataFrame input. You can either write 'mean' or any integer
number for sampling_amount to determine down or upsampling throughout your unique value counts in your target dataset, which
balances your target data automatically to a value assigned in sampling_amount. 
For example, balance(trainingdata, 'target', 'mean') automatically balances target data unique value counts to mean of
target unique values amount. Let's say we have 0, 1, 2, 3 unique values and 5, 10, 10, 50 are their corresponding value counts in target dataset.
As a result of this function, 0, 1, 2, 3 values automatically becomes 19, 19, 19, 19 as value counts.
