# BAR CHARTS

import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

# Use plt.bar to plot numbers of drinks sold on the y-axis. The x-values of the graph should just be the list [0, 1 ... , n-1], where n is the number of categories (drinks) we are plotting. So at x=0, we’ll have the number of cappuccinos sold.
plt.bar(range(len(drinks)), sales)
plt.show()

# Setting labels
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()

# Showing 2 sets of bars side by side

# formula for generating x values of two side by side bars
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]


plt.bar(store1_x, sales1)

n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]
plt.bar(store2_x, sales2)
plt.show()

# Stacked bars
plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)
plt.legend(['Location 1', 'Location 2'], loc=9)
plt.show()

# Error bars
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
plt.show()

# Fill between error bars
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

plt.plot(months, revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = [i * 0.9 for i in revenue]
y_upper = [i * 1.1 for i in revenue]

plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()

# Pie charts

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.axis('equal') #  makes it appear correctly and not at a wird angle
plt.legend(payment_method_names)
plt.show()

# String formatting instructions
# '%0.2f' — 2 decimal places, like 4.08
# '%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. You need two consecutive percent signs because the first one acts as an escape character, so that the second one gets displayed on the chart.
# '%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.

# Histogram

plt.hist(dataset, range=(66,69), bins=40)
# range defines what values to include
# bins defines number of columns

a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)

plt.hist(a, range=(55, 75), bins=20, alpha=0.5, density=True)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5, density=True)
plt.show()
# alpha sets transparency
# density normalises data to similar scale