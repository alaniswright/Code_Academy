# 1 SAMPLE TEST - pval

from scipy.stats import ttest_1samp
import numpy as np

prices = np.genfromtxt("prices.csv")
print(prices)

prices_mean = np.mean(prices)
print("mean of prices: " + str(prices_mean))

# use ttest_1samp to calculate pval
# tstat, pval = ttest_1samp(sample_distribution, expected_mean)
tstat, pval = ttest_1samp(prices, 1000)

# print pval
print(pval)

from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 1000)
  print("Day " + str(i) + ": " + str(round(pval, 2)))

  # BINOMIAL TEST

  #calculate and print sample_size:
sample_size = len(monthly_report)

#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')

#simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size=1, p=[0.1, 0.9])
print(one_visitor)

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
print(simulated_monthly_visitors)

#calculate the number of simulated visitors who made a purchase:
num_purchased = np.sum(simulated_monthly_visitors == 'y')
print(num_purchased)

### Simulating the null distribution

null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)



#calculate the minimum and maximum values in null_outcomes here:
null_min = np.min(null_outcomes)
print(null_min)

null_max = np.max(null_outcomes)
print(null_max)

#calculate the 90% interval here:
np.percentile(null_outcomes, [2.5,97.5])

# Calculate one-sided p-value.
"""
Use null_outcomes to estimate the p-value for a binomial hypothesis test with the following null and alternative hypotheses:
- Null: the probability of a purchase was 10%
- Alternative: the probability of a purchase rate was LESS THAN 10%
In other words, calculate the proportion of values in null_outcomes that are less than or equal to 41 (the observed number of purchases that we calculated earlier)
"""
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes) 
print(p_value)

# Calculating a Two-Sided P-Value
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes)
print(p_value)

# Writing a binomial test function
def simulation_binomial_test(observed_successes, n, p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)


# Binomial testing with scipy
#  For example, with 10 flips of a fair coin (trials), the expected probability of heads is 0.5. Let’s imagine we get 2 heads (observed successes) in 10 flips. Is the coin weighted? The function call for this binomial test would look like:

from scipy import binom_test
p_value = binom_test(2, n=10, p=0.5)
print(p_value) 

# calculate p_value_1sided here: one sided test for less than
p_value_1sided = binom_test(41, n=500, p=0.1, alternative='less')
print(p_value_1sided)

# calculate p_value_1sided here: one sided test for more than
p_value_1sided = binom_test(41, n=500, p=0.1, alternative='greater')
print(p_value_1sided)

# SIGNIFICANCE THRESHOLDS
# when we run a hypothesis test with a significance threshold, the significance threshold is equal to the type I error (false positive) rate for the test. To see this, we can use a simulation.

false_positives = 0
sig_threshold = 0.05
 
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.7, 0.3])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, 0.7)
    if p_val < sig_threshold:
        false_positives += 1
        
print(false_positives/1000) #Output: 0.0512