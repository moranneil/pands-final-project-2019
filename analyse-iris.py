# Neil Moran 18/04/2019
# Python script analyse data using Pandas
# 

#Python librarys Numpy, Pandas and MatplotLib are imported
import numpy as np
import pandas as pd
import matplotlib as plt

#Pandas command is used to read the information from iris-dataset.csv, headers are assigned to each of the five columns.
irisdataset = pd.read_csv('iris-dataset.csv', delimiter=',', names=['Sepal Length', 'Sepal Width', 'Petal Length','Petal Width', 'Species'])

print()
print()
print('This is the first five rows in the Iris Dataset') 
print(irisdataset.head())
print()
print()
print('Summary Statistics for the entire Iris Dataset')
#This command gives a statistical summary of the data that was imported from the CSV file.
print(irisdataset.describe())
print()
print()
print('Number of rows grouped by column heading')
#This command gives statistical info on how many rows in each of the named columns
print(irisdataset.info())
print()
print()
print('Number of rows grouped by column Species')
#This command gives the quantities of samples for each of the values in the column Species
print(irisdataset['Species'].value_counts())
