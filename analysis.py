# Eibhinn Lee
# Fisher's Iris Dataset
# 150 rows of data
# 3 species of Iris (Setosa, Veriscolor, Virginica)
# within each species of Iris = 4 attributes
# Sepal length, Sepal width
# petal length, petal width
# Sepal = modified leaves that encase the developing flower. Usually green.
# Petal = modified leaves that surround the reproductive parts of flowers. Usually colourful.

# Import libraries
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# import dataset "Iris Dataset" textfile.
df = pd.read_csv('Iris_dataset.txt')



# Info of Dataset showing number of values per each variable.
df.info()

df['Species'].value_counts()

df.describe()

df.plot(kind = 'scatter', x = 'SL', y = 'SW')

df.plot(kind = 'scatter', x = 'PL', y = 'PW')



# Breakdown showing total sample size per each Species
sns.countplot('Species', data=df)

# Scatter graph showing each Species 
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("SL v SW")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("SL v PL")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("SL v PW")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("SW v SL")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("SW v PL")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("SW v PW")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("PL v SL")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("PL v SW")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("PL v PW")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("PW v SL")

ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("PW v SW")

ax = df[df.Species=='Iris-setosa'].plot.hist(x='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.hist(x='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.hist(x='PW', color='blue', label='virginica', ax=ax)
ax.set_title("PW v PL")

df.hist(edgecolor='black', linewidth=1.2)
fig=plt.gcf()
fig.set_size_inches(12,6)
plt.show()

plt.figure(figsize = (10, 7)) 
x = df.PW
  
plt.hist(x, bins = 50, color = "green", edgecolor = 'black', linewidth = 1.5) 
plt.title("PW") 
plt.xlabel("PW") 
plt.ylabel("Count") 

plt.figure(figsize = (10, 7)) 
y = df.SW
  
plt.hist(y, bins = 50, color = "red", edgecolor = 'black', linewidth = 1.5) 
plt.title("SW") 
plt.xlabel("SW") 
plt.ylabel("Count") 

plt.figure(figsize = (10, 7)) 
y = df.PL
  
plt.hist(y, bins = 50, color = "orange", edgecolor = 'black', linewidth = 1.5) 
plt.title("PL") 
plt.xlabel("PL") 
plt.ylabel("Count")

plt.figure(figsize = (10, 7)) 
y = df.SL
  
plt.hist(y, bins = 50, color = "BLUE", edgecolor = 'black', linewidth = 1.5) 
plt.title("SL") 
plt.xlabel("SL") 
plt.ylabel("Count")

plt.show()

