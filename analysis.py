# Eibhinn Lee
# Fisher's Iris Dataset
# 150 rows of data
# 3 species of Iris (Setosa, Veriscolor, Virginica)
# within each species of Iris = 4 attributes
# Sepal length, Sepal width
# petal length, petal width
# Sepal = modified leaves that encase the developing flower. Usually green.
# Petal = modified leaves that surround the reproductive parts of flowers. Usually colourful.
# SL = Sepal length
# SW = Sepal Width
# PL = Petal length
# PW = Petal Width

# Import libraries
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# import dataset "Iris Dataset" textfile.
df = pd.read_csv('Iris_dataset.txt')

# Info of Dataset showing number of values per each variable.
df.info()

# Total number of Species
Irisdata = df['Species'].value_counts()
print(Irisdata)

# Breakdown showing total sample size per each Species
sns.countplot('Species', data=df)
plt.savefig("Total of each Species")

# Pairplot showing a combination of all variables in scatter plots and histgrams.
sns.set()
sns.pairplot(df[['SL', 'SW', 'PL', 'PW', 'Species']], hue="Species", diag_kind="hist")
plt.savefig("Pairplot")
# Scatter graph showing each Species 
# 1
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal length v Sepal Width")
plt.savefig("Sepal length v Sepal Width")
# 2
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal length v Petal length")
plt.savefig("Sepal length v Petal length")
#3
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal length v Petal Width")
plt.savefig("Sepal length v Petal Width")
# 4
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal Width v Sepal length")
plt.savefig("Sepal Width v Sepal length")
# 5
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal Width v Petal length")
plt.savefig("Sepal Width v Petal length")
# 6
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal Width v Petal Width")
plt.savefig("Sepal Width v Petal Width")
# 7
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("Petal length v Sepal length")
plt.savefig("Petal length v Sepal length")
# 8
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("Petal length v Sepal Width")
plt.savefig("Petal length v Sepal Width")
# 9
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("Petal length v Petal Width")
plt.savefig("Petal length v Petal Width")
# 10
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("Petal Width v Sepal length")
plt.savefig("Petal Width v Sepal length")
# 11
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("Petal Width v Sepal Width")
plt.savefig("Petal Width v Sepal Width")
# 12
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("Petal Width v Petal length")
plt.savefig("Petal Width v Petal length")

# Histograms on single graph showing each variable
df.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)
plt.savefig("Histogram showing each varaible on a single graph")

# Histogram of each variable
plt.figure(figsize = (10, 7)) 
y = df.PW

plt.hist(y, bins = 50, color = "green", edgecolor = 'black', linewidth = 1.5) 
plt.title("Petal Width") 
plt.xlabel("PW") 
plt.ylabel("Count")
plt.savefig("PW Hist")

plt.figure(figsize = (10, 7)) 
y = df.SW
  
plt.hist(y, bins = 50, color = "red", edgecolor = 'black', linewidth = 1.5) 
plt.title("Sepal Width") 
plt.xlabel("SW") 
plt.ylabel("Count")
plt.savefig("SW Hist")

plt.figure(figsize = (10, 7)) 
y = df.PL
  
plt.hist(y, bins = 50, color = "orange", edgecolor = 'black', linewidth = 1.5) 
plt.title("Petal Length") 
plt.xlabel("PL") 
plt.ylabel("Count")
plt.savefig("PL Hist")

plt.figure(figsize = (10, 7)) 
y = df.SL
  
plt.hist(y, bins = 50, color = "BLUE", edgecolor = 'black', linewidth = 1.5) 
plt.title("Sepal Length") 
plt.xlabel("SL") 
plt.ylabel("Count")
plt.savefig("SL Hist")

plt.show()

