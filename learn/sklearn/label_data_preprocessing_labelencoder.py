# In this exercise we'll load the titanic data (from Project 0)
# And then perform one-hot encoding on the feature names

import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('titanic_data.csv')
# Limit to categorical data
X = X.select_dtypes(include=[object])

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# Create a LabelEncoder object, which will turn all labels present in
#       in each feature to numbers.
# HINT: Use LabelEncoder()
le = LabelEncoder()


# For each feature in X, apply the LabelEncoder's fit_transform
#       function, which will first learn the labels for the feature (fit)
#       and then change the labels to numbers (transform).
X = X.apply(le.fit_transform)

# Create a OneHotEncoder object, which will create a feature for each
#       label present in the data.
# HINT: Use OneHotEncoder()
ohe = OneHotEncoder()

# Apply the OneHotEncoder's fit_transform function to all of X, which will
#       first learn of all the (now numerical) labels in the data (fit), and then
#       change the data to one-hot encoded entries (transform).

# HINT: Use fit_transform on X using the OneHotEncoder() object
xt = ohe.fit_transform(X)
onehotlabels = xt