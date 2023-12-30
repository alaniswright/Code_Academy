# ASSOCIATIONS: QUANTITATIVE AND CATEGORICAL

import numpy as np
import pandas as pd
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#calculate means for each group:
scores_urban_mean = np.mean(scores_urban)
scores_rural_mean = np.mean(scores_rural)

#print mean scores:
print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)

#calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

#print mean difference
print('Mean difference:')
print(mean_diff)

#calculate medians for each group:
scores_urban_median = np.median(scores_urban)
scores_rural_median = np.median(scores_rural)

#print median scores
print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

#calculate median difference
median_diff = scores_urban_median - scores_rural_median

#print median difference
print('Median difference:')
print(median_diff)

# ---
# 3

#create the boxplot here:
sns.boxplot(data = students, x = 'address', y = 'G3')
plt.show()

# ---
# 4

#create the overlapping histograms here
# normed=True makes Y axis proportional
# alpha=0.5 makes boxes transparant at 50%
plt.hist(scores_urban , color="blue", label="Urban", normed=True, alpha=0.5)
plt.hist(scores_rural , color="red", label="Rural", normed=True, alpha=0.5)
plt.legend()
plt.show()

#Exploring Non-Binary Categorical Variables
#create the box-plot here:
sns.boxplot(data = students, x = 'Fjob', y = 'G3')
plt.show()



# ASSOCIATIONS: TWO QUANTITATIVE VARIABLES

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.xlabel('Beds')
plt.ylabel('Area (Square Feet)')
plt.show()

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.beds, housing.sqfeet)

# [0][1] or [1][0] is the covariance
print(cov_mat_sqfeet_beds)

# store the covariance as cov_sqfeet_beds
cov_sqfeet_beds = cov_mat_sqfeet_beds[0][1]

# Correlation
# calculate corr_sqfeet_beds and print it out:
from scipy.stats import pearsonr
corr_sqfeet_beds, p = pearsonr(housing.beds, housing.sqfeet)
print(corr_sqfeet_beds) 

# create the scatter plot here:
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.xlabel('Beds')
plt.ylabel('Area (Square Feet)')
plt.show()


# ASSOCIATIONS: TWO CATEGORICAL VARIABLES

npi = pd.read_csv("npi_sample.csv")

#Contingency Tables: Frequencies
special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq/len(npi)

# print out special_authority_prop
print(special_authority_prop)

# Marginal proportions

# calculate and print authority_marginals
authority_marginals = special_authority_prop.sum(axis=0)
print(authority_marginals)


# calculate and print special_marginals
special_marginals =  special_authority_prop.sum(axis=1)
print(special_marginals)

# Expected Contingency Tables
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print("observed contingency table:")
print(special_authority_freq)

# calculate the expected contingency table if there's no association and save it as expected
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)

# print out the expected frequency table
print("expected contingency table (no association):")
print(np.round(expected))

# The Chi-Square Statistic summarises how different 2 tables are.  
# The interpretation of the Chi-Square statistic is dependent on the size of the contingency table. For a 2x2 table (like the one we’ve been investigating), a Chi-Square statistic larger than around 4 would strongly suggest an association between the variables. 
# calculate the chi squared statistic and save it as chi2, then print it:
special_authority_freq = pd.crosstab(npi.special, npi.authority)

chi2, pval, dof, expected = chi2_contingency(special_authority_freq)
print(chi2)