# Eibhinn Lee
#Programming and Scripting Project 2020
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


outF = open("analysis.txt", "w")
# Import libraries being used
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# import dataset "Iris Dataset" textfile.
df = pd.read_csv('Iris_dataset.txt')

# Info of Dataset showing number of values per each variable.
df.info()
outF.write("Total amount per each variable")
outF.write(">Sepal length = 150 values\n")
outF.write(">Sepal width = 150 values\n")
outF.write(">Petal length = 150 values\n")
outF.write(">Petal width = 150 values\n")
# Total number of Species
Irisdata = df['Species'].value_counts()
print(Irisdata)
outF.write("Iris-Setosa, Iris-Versicolor & Iris-Virginica all have a sample size of 50\n")
# Breakdown showing total sample size per each Species
sns.countplot('Species', data=df)
plt.savefig("Total of each Species")
outF.write("Visual display showing Iris-Setosa, Iris-Versicolor & Iris-Virginica all have a sample size of 50\n")

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
outF.write("Sepal length v Sepal Width:         ")
outF.write("Virginica & Versicolor SL/SW seem to be similar length as many overlap unlike the setosa\n")

# 2
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal length v Petal length")
plt.savefig("Sepal length v Petal length")
outF.write("Sepal length v Petal length:")
outF.write("Setosa have a thin cluster of petals compared to other species, more a variable range of sepal lengths also amongst the other variables.\n")
outF.write(">setosa have quite a narrow range of petals and sepals\n")
#3
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal length v Petal Width")
plt.savefig("Sepal length v Petal Width")
outF.write("Sepal length v Petal Width:")
outF.write("sepal length and petal width are more spaced out, setosa range is fairly clustered together\n")
# 4
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal Width v Sepal length")
plt.savefig("Sepal Width v Sepal length")
outF.write("Sepal Width v Sepal length:")
outF.write("One of the more decaorated graph's on show, setosa sepal's are wider while the sepal's on the other species are longer\n")
# 5
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal Width v Petal length")
plt.savefig("Sepal Width v Petal length")
outF.write("Sepal Width v Petal length:")
outF.write("Setosa have a wider range of values but narrow range of lengths of petals and it is the opposite of the other species\n")

# 6
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SW', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SW', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SW', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("Sepal Width v Petal Width")
plt.savefig("Sepal Width v Petal Width")
outF.write("Sepal Width v Petal Width:")
outF.write("Setosa have a wider range of values but narrow range of width of petals and it is the opposite of the other species\n")

# 7
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("Petal length v Sepal length")
plt.savefig("Petal length v Sepal length")
outF.write("Sepal length v Sepal Width:")
outF.write("Setosa's length of petals and sepals are clearly smaller than other species\n")

# 8
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("Petal length v Sepal Width")
plt.savefig("Petal length v Sepal Width")
outF.write("Petal length v Sepal Width:")
outF.write("Virginica and versicolor have longer petals but the setosa while not as long, as more of a wide range of sepals among the sample\n")

# 9
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PL', y='PW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PL', y='PW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PL', y='PW', color='blue', label='virginica', ax=ax)
ax.set_title("Petal length v Petal Width")
plt.savefig("Petal length v Petal Width")
outF.write("Petal length v Petal Width:")
outF.write("Both petal variables for setosa are the smallest approx >2cm long & >1cm wide. Both other species are greater than 1 cm width and 3cm long\n")

# 10
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='SL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='SL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='SL', color='blue', label='virginica', ax=ax)
ax.set_title("Petal Width v Sepal length")
plt.savefig("Petal Width v Sepal length")
outF.write("Petal Width v Sepal length:")
outF.write("Some small overlapping between Versicolor and virginica and show larger petals and sepals compared to the setosa\n")

# 11
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='SW', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='SW', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='SW', color='blue', label='virginica', ax=ax)
ax.set_title("Petal Width v Sepal Width")
plt.savefig("Petal Width v Sepal Width")
outF.write("Petal Width v Sepal Width:")
outF.write("The Setosa sepal clusters mainly between 3/4 cm but is short at approx 0.5cm while the other species range more than 1 cm\n")

# 12
ax = df[df.Species=='Iris-setosa'].plot.scatter(x='PW', y='PL', color='red', label='setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PW', y='PL', color='green', label='versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='PW', y='PL', color='blue', label='virginica', ax=ax)
ax.set_title("Petal Width v Petal length")
plt.savefig("Petal Width v Petal length")
outF.write("Petal Width v Petal length:")
outF.write("Setosa  clearly have the smallest petal length and width, the graph shows a clear difference compared to the other species\n")

outF.write("Conclusion:")
outF.write("There is clear differentiation among species, predominantly the setosa who often finds itself on its own away from the other species.\n")
outF.write("The virginica and versicolor while show a difference, the likeihood of any species overlapping somewhat would be between those species and not the setosa.\n")
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

outF.close()
plt.show()


