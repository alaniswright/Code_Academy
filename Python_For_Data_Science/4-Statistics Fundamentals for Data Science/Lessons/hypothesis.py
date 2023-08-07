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