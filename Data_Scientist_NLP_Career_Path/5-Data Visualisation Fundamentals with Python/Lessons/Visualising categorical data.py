# Bar charts with Seaborn

import codecademylib3
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("games.csv")
print(df.head())

sns.countplot(df["victory_status"])

# Bar chart ordering

value_order = ["NOT ENOUGH DATA", "VERY WEAK", "WEAK", "NEUTRAL", "STRONG", "VERY STRONG"]

type_of_data = "ordinal"

sns.countplot(df["Supportive Environment"], order=value_order) # orders by value order
plt.xticks(rotation=30) # rotates the xticks
plt.show()

# Pie charts

import matplotlib.pyplot as plt
import pandas as pd
import codecademylib3

water_usage = pd.read_csv("water_usage.csv")
print(water_usage.head())

wedge_sizes = water_usage['prop']
pie_labels = water_usage['water_source']

plt.pie(wedge_sizes, labels = pie_labels)
plt.axis('equal')
plt.title('Distribution of House Water Usage')
plt.show()


