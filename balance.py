def balance(train, target, sampling_amount):
# This function takes training data and target column name as DataFrame input. You can either write 'mean' or any integer
# number for sampling_amount to determine down or upsampling throughout your unique value counts in your target dataset, which
# balances your target data automatically to a value assigned in sampling_amount. 
# For example, balance(trainingdata, 'target', 'mean') automatically balances target data unique value counts to mean of
# target values amount. Let's say we have 0, 1, 2, 3 unique values and 5, 10, 10, 50 are the value counts in target dataset.
# As a result of this function, 0, 1, 2, 3 values automatically becomes 19, 19, 19, 19 as value counts.
    degerler = train[target].value_counts()
    if sampling_amount is 'mean' or 'Mean':
        rounded = int(np.round(degerler.values.mean()))
    else:
        rounded = sampling_amount
    for i in range(len(degerler)):
        gg = train[train['open_channels']==i]
        train = train.drop(train[train['open_channels']==i].index)
        if degerler[i]<=degerler.mean():
            labelt_upsampled = gg.sample(rounded, replace=True)
            train = pd.concat([train, labelt_upsampled])
        else:
            labelt_downsampled = gg.sample(rounded)
            train = pd.concat([train,labelt_downsampled])
    return train
