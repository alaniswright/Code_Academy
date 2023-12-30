# Random variable dice similuator

import numpy as np

# create 6 sided "die"
die_6 = range(1, 7)

# set number of rolls
num_rolls = 5

# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# create 12-sided "die"
die_12 = range(1, 13)

# roll the 12-sided "die" 10 times
num_rolls = 10
results_2 = np.random.choice(die_12, size = num_rolls, replace = True)
print(results_2)

# CALCULATION PROBABILITY MASS FUNCTION
# **probability mass function** is a function that gives the probability that a [discrete random variable](https://en.wikipedia.org/wiki/Discrete_random_variable "Discrete random variable") is exactly equal to some value.
# eg. probability of 6 heads being rolled when rolling a dice 10 times

# x: the value of interest
# n: the number of trials
# p: the probability of success

# import necessary library
import scipy.stats as stats
 
# st.binom.pmf(x, n, p)
# look for 6 heads when flipping a coin 10 times, 
print(stats.binom.pmf(6, 10, 0.5))

# Probability Mass Function Over a Range using Python

## probability of observing between 4 to 6 heads from 10 coin flips
prob_1 = stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5) + stats.binom.pmf(6, n=10, p=.5)
print(prob_1)

## Use the 1 minus the sum of some values of stats.binom.pmf() method to set prob_2 to the probability of observing more than 2 heads from 10 coin flips.
prob_2 = 1 - (stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5))
print(prob_2)

# CUMULATIVE DISTRIBUTION FUNCTION
# gives the probability of observing a specific value OR LESS
# The value of a cumulative distribution function at a given value is equal to the sum of the probabilities lower than it, with a value of 1 for the largest possible number.

import scipy.stats as stats
 
print(stats.binom.cdf(6, 10, 0.5))


# PROBABILITY DENSITY FUNCTION
# define the probability distributions of continuous random variables and span across all possible values that the given random variable can take on

# x: the value of interest
# loc: the mean of the probability distribution
# scale: the standard deviation of the probability distribution

import scipy.stats as stats
 
# stats.norm.cdf(x, loc, scale)
# probability that a woman is less than 158cm tall, when mean height is 167.64 and standard deviation is 8
print(stats.norm.cdf(158, 167.64, 8))

# greater than 172 cm...
print(1 - stats.norm.cdf(172, 167.74, 8))

# POISSON DISTRIBUTION
# the number of times a certain event occurs within a fixed time or space interval. 
# we expect it to rain 10 times in the next 30 days. 
# The number of times it rains in the next 30 days is “Poisson distributed” with lambda = 10. 
# We can calculate the probability of exactly 6 times of rain as follows:

import scipy.stats as stats
# expected value = 10, probability of observing 6
stats.poisson.pmf(6, 10)

# expected value = 10, probability of observing more than 15
1 - stats.poisson.pmf(15, 10)

# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

# print variance of rand_vars_7
print(np.var(rand_vars_7))

# print minimum and maximum of rand_vars_7
print(min(rand_vars_7), max(rand_vars_7))

# Probability of observing 4 or fewer defects in a day, when 7 is lamda of defects
stats.poisson.cdf(4, 7)



# VARIANCE OF THE BINOMIAL DISTRIBUTION
# Variance(#ofHeads)=Var(X)=n×p×(1−p)

# DISTRIBUTIONS
# stats.binom = Binomial distribution is a common discrete distribution used in statistics, as opposed to a continuous distribution, such as normal distribution. This is because binomial distribution only counts two states, typically represented as 1 (for a success) or 0 (for a failure), given a number of trials in the data.
# stats.poisson =  A Poisson distribution is a discrete probability distribution. It gives the probability of an event happening a certain number of times (k) within a given interval of time or space.
# stats.norm = Normal distribution is a type of continuous probability distribution for a real-valued random variable.

# METHODS
# .cdf = cumulative distribution function = tells us the probability that a random variable takes on a value less than or equal to some value
# .rvs = random value simulator = generate the random variate from generalized normal distribution by using stats
# .ppf = takes the probability value and returns cumulative value corresponding to probability value of the distribution
# .pmf = probability mass function = a function that gives the probability that a [discrete random variable](https://en.wikipedia.org/wiki/Discrete_random_variable "Discrete random variable") is exactly equal to some value.