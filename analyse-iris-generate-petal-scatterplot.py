# Neil Moran 22/04/2019
# Python script analyse data using Pandas
# 

#Python librarys Numpy, Pandas and MatplotLib are imported
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pandas command is used to read the information from iris-dataset.csv, headers are assigned to each of the five columns.
irisdatasetscatter = pd.read_csv('iris-dataset.csv', delimiter=',', names=['Sepal_Length', 'Sepal_Width', 'Petal_Length','Petal_Width', 'Species'])



#Generating Petal Scatterplot section

#Seaborn default graphic enhancement are used, these display a enhanced plot compared to matplotlib
sns.set()
#This line assigns the x-axis to a column 'Petal_Length', y-axis to the column 'Petal_Width', grouped by the column by 'Species') 
ax = sns.scatterplot(x=irisdatasetscatter.Petal_Length, y=irisdatasetscatter.Petal_Width, hue=irisdatasetscatter.Species, style=irisdatasetscatter.Species)
#This command give the Scatterlot a title
plt.title('Iris Dataset Petal Scatterplot')
#This command labels the X-axis
plt.xlabel('Petal Length CM')
#This command labels the Y-axis
plt.ylabel('Petal Width CM')
#This command displays the plot.
plt.show()
