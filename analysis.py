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

df.plot(kind = 'scatter', x = 'SL', y = 'SW')
sns.countplot('Species', data=df)
plt.show()

