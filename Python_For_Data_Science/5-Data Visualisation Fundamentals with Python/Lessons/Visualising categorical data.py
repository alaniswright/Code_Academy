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

