import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset: house sizes and number of bedrooms as features, and prices as the target variable
# Feature 1
house_sizes = np.array([550, 600, 650, 700, 750, 800, 850, 900, 950, 1000])

# Complete by student (Feature 2)
# Simulate num_bedrooms, you may create more relevant features by your own
num_bedrooms = np.array([, , , , , , , , , ])

# add more feature, e.g number of bathrooms, years etc

# You shall modify the values of label
prices = np.array([300000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000])