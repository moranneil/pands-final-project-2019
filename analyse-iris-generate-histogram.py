# Neil Moran 18/04/2019
# Python script imports Iris Dataset from csv file 
# Generates Histogram once the data is imported from the csv file

#Python librarys Numpy, Pandas, MatplotLib and Seaborn are imported
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pandas command is used to read the information from iris-dataset.csv, headers are assigned to each of the five columns.
irisdataset = pd.read_csv('iris-dataset.csv', delimiter=',', names=['Sepal Length', 'Sepal Width', 'Petal Length','Petal Width', 'Species'])

#Generating Histogram section

#Seaborn default graphic enhancement is used, these display a enhanced plot compared to matplotlib
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
