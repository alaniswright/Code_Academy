import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

## Plotting the Population Distribution
sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf() # close this plot

samp_size = 10
# Generate our random sample below
sample = np.random.choice(np.array(population), samp_size, replace = False)

### Define sample mean below
sample_mean = round(np.mean(sample),3)

### Uncomment the lines below to plot the sample data:
sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()

# SAMPLING DISTRIBUTIONS

salmon_population = population['Salmon_Weight']
 
sample_size = 50
sample_means = []
 
# loop 500 times to get 500 random sample means
for i in range(500):
  # take a sample from the data:
  samp = np.random.choice(salmon_population, sample_size, replace = False)
  # calculate the mean of this sample:
  this_sample_mean = np.mean(samp)
  # append this sample mean to a list of sample means
  sample_means.append(this_sample_mean)
 
# plot all the sample means to show the sampling distribution
sns.histplot(sample_means, stat='density')
plt.title("Sampling Distribution of the Mean")
plt.show()

# CENTRAL LIMIT THEOREM
# allows us to specifically describe the sampling distribution of the mean.

"""
In order to review, let’s consider an example from a restaurant serving quarter-pounder burgers. Their quarter-pounders weigh an average of 0.25 lbs with a standard deviation of 0.2 lbs.

Let’s say we weigh all their burgers that they cook for dinner on a given night. 64 people order quarter-pounders. What is the probability that the mean will be 0.24 lbs or less?
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import codecademylib3

# Set up parameters here:
x = 0.24 # weight average burger from sample must be below
population_mean = 0.25 # mean weight of burger
population_std_dev = 0.2 # std dev or burger weight
samp_size = 64 # number of burgers

### Below is code to create simulated dataset and calculate Standard Error
standard_error = population_std_dev / (samp_size**.5)

this_cdf = round(stats.norm.cdf(x,population_mean,standard_error),3)

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

# Simulate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlabel("")
plt.show()
plt.clf()

# Plot the sampling distribution
sns.histplot(sample_means, stat = 'density')
plt.axvline(x,color='r',linestyle='dashed')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}\n CDF for x={x}: {this_cdf}")
plt.xlabel("")
plt.show()