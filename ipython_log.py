# IPython log file

get_ipython().run_line_magic('logstart', '')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df
df = pd.read_csv('Iris_dataset.txt')
df
df['PW']
df.info()
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y ='SW', color ='red', label = 'setosa')
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y ='SW', color ='red', label = 'setosa') df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='SL', color = 'blue', label = 'versicolor', ax = ax)
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y ='SW', color ='red', label = 'setosa')
x = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y ='SW', color ='red', label = 'setosa')
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y ='SW', color ='red', label = 'setosa') df[df.Species     ...: =='Iris-versicolor'].plot.scatter(x='SW', y='SL', color = 'blue', label = 'versicolor', ax = ax)
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW',                                                     color='red', label='setosa')      df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW',                                                     color='green', label='versicolor', ax=ax)      df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW',                                                      color='blue', label='virginica', ax=ax)
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW',                                                     color='red', label='setosa')      df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW',                                                     color='green', label='versicolor', ax=ax)      df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW',                                                      color='blue', label='virginica', ax=ax)
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW',                                                                                               color='red', label='setosa')                                  df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW',                                                                                                color='green', label='versicolor', ax=ax)                     df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW',                                                                                               color='blue', label='virginica', ax=ax)
sns.FaceGrid(df, hue="Species",size = 4).map(plt.scatter,"SW","SL").add_legend
sns.FaceGrid(df, hue="Species",size = 4).map(plt.scatter,"SW","SL").add_legend
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW',                                                     color='red', label='setosa')
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW', color='red', label='setosa')
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW', color='red', label='setosa')
ax
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW',                                                     color='red', label='setosa') df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW',                                                 color='green', label='versicolor', ax=ax) df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW',                                                 color='blue', label='virginica', ax=ax)
df
pp = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='PW',                                                     color='red', label='setosa') df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='PW',                                                 color='green', label='versicolor', ax=ax) df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='PW',                                                 color='blue', label='virginica', ax=ax)
df.plot(kind = 'scatter', x = 'SL', y = 'SW')
plt.scatter(group.index)
plot.scatter(group.index)
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW',                                                     color='red', label='setosa') df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW',                                                 color='green', label='versicolor', ax=ax)
df["species"].value_counts()
sns.FacetGrid(df, hue="species", size=5) \    .map(plt.scatter, "sepal length (cm)", "sepal width (cm)") \    .add_legend()
sns.pairplot(df.drop("target", axis=1), hue="species", size=3)
sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Species", size = 4).map(plt.scatter,"SL","SW").add_legend()
df
exit()
