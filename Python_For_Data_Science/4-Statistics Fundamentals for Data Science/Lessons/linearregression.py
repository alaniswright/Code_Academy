# Fitting a Linear Regression Model in Python
"""
There are a number of Python libraries that can be used to fit a linear regression, but in this course, we will use the OLS.from_formula() function from statsmodels.api because it uses simple syntax and provides comprehensive model summaries.
"""

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# create a linear regression model that predicts student score using hours_studied as a predictor and save the result as a variable named model.
model = sm.OLS.from_formula('score ~ hours_studied', data = students)

# Fit the model here:
results = model.fit()

# Print the coefficients here:
print(results.params)

# Calculate and print `pred_3hr` here:
pred_3hr = results.params[1]*3 + results.params[0]
print(pred_3hr)

# Calculate and print `pred_5hr` here:
newdata = {"hours_studied":[5]}
pred_5hr = results.predict(newdata)
print(pred_5hr)

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Calculate `fitted_values` here:
fitted_values = results.predict(students)
print(fitted_values.head())

# Calculate `residuals` here:
residuals = students.score - fitted_values
print(residuals.head())

# Test normality assumption
# Look for normal distribution
# Plot a histogram of the residuals here:
plt.hist(residuals)
plt.show()
plt.clf()

# Test Homoscedasticity assumption
# Homoscedasticity is a fancy way of saying that the residuals have equal variation across all values of the predictor variable.
# Look for even results either side of 0. No pattern in scatter plot
# Plot the residuals against the fitted vals here:
plt.scatter(fitted_values, residuals)
plt.show()