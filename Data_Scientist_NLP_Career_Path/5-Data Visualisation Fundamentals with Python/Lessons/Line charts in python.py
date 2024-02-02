import codecademylib
from matplotlib import pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6] # a variable of x values
money_spent = [10, 12, 12, 10, 14, 22, 24] # a variable of y values
plt.plot(days, money_spent) # plt is the name we have given to the Matplotlib module we have imported at the top of the code
plt.show() # will actually display the graph

# Multiple lines

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()


# Styling. See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot for options
# Colours
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')
# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')
# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(revenue, time, color='purple', linestyle='--')
plt.plot(costs, time, color='#82edc9', marker='s')
plt.show()

# Zoom in and our via changing axis
plt.axis([0, 12, 2900, 3100])

# Labels and title
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My last Twelve years of Coffee Drinking')

# Subplots
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1,2,1)
plt.plot(temperature, months)

plt.subplot(1,2,2)
plt.plot(temperature, flights_to_hawaii, 'o') # Draws scatterplot

plt.show()

# Customise spacing
"""
left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
top — the top margin, with a default of 0.9
wspace — the horizontal space between adjacent subplots, with a default of 0.2
hspace — the vertical space between adjacent subplots, with a default of 0.2
"""
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# Subplot 1
plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

# Subplot 2
plt.subplot(2, 2, 3)
plt.plot(x, parabola)

# Subplot 3
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()

# Legends
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
plt.legend(['parabola', 'cubic'], loc=6)
plt.show()

# Location of legend can vary
"""
Number Code	String
0	best
1	upper right
2	upper left
3	lower left
4	lower right
5	right
6	center left
7	center right
8	lower center
9	upper center
10	center
"""

# Modify ticks
# Modify unit of measurement on x and y axis, as well as their labels
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
plt.plot(months, conversion)
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])
plt.show()

# Close before starting new figures so data isn't carried over
plt.close('all')

# Create plot of specific size and download as file
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')
plt.show()

plt.figure(figsize=(7, 3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')
plt.show()

# Exercise

import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# create your figure here
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1, 2, 1)
x_values = range(len(months))
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.xlabel('Month')
plt.ylabel('Visits per month')
plt.plot(x_values, visits_per_month, marker='o')
plt.title('Visits by month')
ax2 = plt.subplot(1, 2, 2)
plt.plot(x_values, key_limes_per_month, color='green')
plt.plot(x_values, persian_limes_per_month, color='blue')
plt.plot(x_values, blood_limes_per_month, color='red')
plt.legend(['Key limes', 'Persian limes', 'Blood limes'], loc=6)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.xlabel('Month')
plt.title('Key lime sales by month')
plt.savefig('key_limes.png')
plt.show()