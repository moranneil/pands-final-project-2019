# Neil Moran 18/04/2019
# Python script analyse data using Pandas
# 

#Python librarys Numpy, Pandas and MatplotLib are imported
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pandas command is used to read the information from iris-dataset.csv, headers are assigned to each of the five columns.
irisdataset = pd.read_csv('iris-dataset.csv', delimiter=',', names=['Sepal Length', 'Sepal Width', 'Petal Length','Petal Width', 'Species'])

print()
print()
print('This is the first five rows in the Iris Dataset')
print()
print(irisdataset.head())
print()
print()
print('Summary Statistics for the entire Iris Dataset')
print()
#This command gives a statistical summary of the data that was imported from the CSV file.
print(irisdataset.describe())
print()
print()
print('Number of rows grouped by column heading')
print()
#This command gives statistical info on how many rows in each of the named columns
print(irisdataset.info())
print()
print()
print('Number of rows grouped by column Species')
print()
#This command gives the quantities of samples for each of the values in the column Species
print(irisdataset['Species'].value_counts())


#Generating Histogram section

#Seaborn default graphic enhancement are used, these display a enhanced plot compared to matplotlib
sns.set()
#irisdataset is used from the program analyse-iris.py, the edge line of the bins are red and they are 10 bins per plot
#This command also generates a plot for each colum with numerical values, Sepal Length, Sepal Width, Petal Length and Petal Width
irisdataset.hist(edgecolor='red', bins=10)
#This command improved the scaling on the axis of the plots
fig = plt.gcf()
#This command sets the size of the figure
fig.set_size_inches(12,6)
#This command displays the plot.
plt.show()
