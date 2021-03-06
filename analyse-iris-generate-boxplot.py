# Neil Moran 18/04/2019
# Python script imports Iris Dataset from csv file 
# Generates Boxplot once the data is imported from the csv file 

#Python librarys Numpy, Pandas MatplotLib and Seaborn are imported
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pandas command is used to read the information from iris-dataset.csv, headers are assigned to each of the five columns.
irisdataset = pd.read_csv('iris-dataset.csv', delimiter=',', names=['Sepal Length', 'Sepal Width', 'Petal Length','Petal Width', 'Species'])



#Generating Boxplot section

#Seaborn default graphic enhancement is used, this displays a enhanced plot compared to matplotlib
sns.set()
#This command also generates a Boxplot for each colum with numerical values, Sepal Length, Sepal Width, Petal Length and Petal Width
irisdataset.boxplot()
#This command give the Boxplot a title
plt.title('Iris Dataset Boxplot')
#This command labels the Y-axis
plt.ylabel('Centimetres')
#This command displays the plot.
plt.show()
