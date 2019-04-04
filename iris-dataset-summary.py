# Neil Moran 04/04/2019
# Python script to summarise the Iris Dataset
# The script calculates the min, max and mean value of each of the four columns on the Iris Dataset using Numpy

import numpy

#Read the data fro the CSV file in to an array
irisdata = numpy.genfromtxt("iris-dataset.csv", delimiter=',')

#Assign the first column of the dataset to the array septallength
sepallength = irisdata[:,0]

#The min, max and average septallength is calculated, the mean calculation is rounded to two decimal places.
minsepallength = numpy.min(irisdata[:,0])
maxsepallength = numpy.max(irisdata[:,0])
meansepallength = numpy.mean(irisdata[:,0])
meansepallengthdec2 = round(meansepallength,2)

##Print the min, max and average sepal length rounded to two decmial places
print("********************************")
print(f"The minimum sepal length is {minsepallength}")
print(f"The maximum sepal length is {maxsepallength}")
print(f"The average sepal length is {meansepallengthdec2}")
print("********************************")

#Assign the second column of the dataset to the array septalwidth
sepalwidth = irisdata[:,1]

#The min, max and average septalwidth is calculated, the mean calculation is rounded to two decimal places.
minsepalwidth = numpy.min(irisdata[:,1])
maxsepalwidth = numpy.max(irisdata[:,1])
meansepalwidth = numpy.mean(irisdata[:,1])
meansepalwidthdec2 = round(meansepalwidth,2)

#Print the min, max and average sepal width rounded to two decmial places
print(f"The minimum sepal width is {minsepalwidth}")
print(f"The maximum sepal width is {maxsepalwidth}")
print(f"The average sepal width is {meansepalwidthdec2}")
print("********************************")

#Assign the third column of the dataset to the array septallength
petallength = irisdata[:,2]

#The min, max and average of the petallength is calculated, the mean calculation is rounded to two decimal places.
minpetallength = numpy.min(irisdata[:,2])
maxpetallength = numpy.max(irisdata[:,2])
meanpetallength = numpy.mean(irisdata[:,2])
meanpetallengthdec2 = round(meanpetallength,2)

##Print the average petal length rounded to two decmial places
print(f"The minimum petal length is {minpetallength}")
print(f"The maximum petal length is {maxpetallength}")
print(f"The average petal length is {meanpetallengthdec2}")
print("********************************")

#Assign the fourth column of the dataset to the array petalwidth
petalwidth = irisdata[:,3]

#The average of the petalwidth is calculated, the mean calculation is rounded to two decimal places.
minpetalwidth = numpy.min(irisdata[:,3])
maxpetalwidth = numpy.max(irisdata[:,3])
meanpetalwidth = numpy.mean(irisdata[:,3])
meanpetalwidthdec2 = round(meanpetalwidth,2)

#Print the average sepal width rounded to two decmial places
print(f"The minimum petal width is {minpetalwidth}")
print(f"The maximum petal width is {maxpetalwidth}")
print(f"The average petal width is {meanpetalwidthdec2}")
print("********************************")
