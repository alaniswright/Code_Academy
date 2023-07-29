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





# ASSOCIATIONS: TWO CATEGORICAL VARIABLES
