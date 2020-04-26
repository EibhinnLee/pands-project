# Eibhinn Lee
# Fisher's Iris Dataset
# 150 rows of data
# 3 species of Iris (Setosa, Veriscolor, Virginica)
# within each species of Iris = 4 attributes
# Sepal length, Sepal width
# petal length, petal width
# Sepal = modified leaves that encase the developing flower. Usually green.
# Petal = modified leaves that surround the reproductive parts of flowers. Usually colourful.


import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Iris_dataset.txt')
df.info()
df.plot(kind = 'scatter', x = 'SL', y = 'SW')

sns.countplot('Species', data=df)

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("scatter")


plt.show()