# Neil Moran 25/04/2019
# Python script imports Iris Dataset from csv file 
# Generates Pairplot once the data is imported from the csv file 

#Python librarys Numpy, Pandas, MatplotLib and Seaborn are imported
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pandas command is used to read the information from iris-dataset.csv, headers are assigned to each of the five columns.
irisdataset = pd.read_csv('iris-dataset.csv', delimiter=',', names=['Sepal Length', 'Sepal Width', 'Petal Length','Petal Width', 'Species'])



#Generating Iris Dataset Pairplot section

#Seaborn default graphic enhancement are used, these display a enhanced plot compared to matplotlib
sns.set()
#This line used the seaborn pairplot function to graph the data that was imported to the irisdataset variable using the column Species to sort the results using the default palette colours.
pair = sns.pairplot(irisdataset, hue="Species")
#The 'pair' pairplot from the command above is displayed to the screen.
plt.show(pair)
