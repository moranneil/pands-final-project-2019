# Neil Moran 04/04/2019
# Python script to summarise the Iris Dataset
# Calculates the min, max & mean value of each of the four numerical columns of the Iris Dataset using Numpy.

import numpy

#Read the data fro the CSV file in to an array
irisdata = numpy.genfromtxt("iris-dataset.csv", delimiter=',')

#Assign the first column of the dataset to the array septallength
sepallength = irisdata[:,0]

#The min, max and average septallength is calculated, the mean calculation is rounded to two decimal places.
minsepallength = numpy.min(irisdata[:,0])
maxsepallength = numpy.max(irisdata[:,0])
meansepallength = numpy.mean(irisdata[:,0])
stdsepallength = numpy.std(irisdata[:,0])
meansepallengthdec2 = round(meansepallength,2)
stdsepallengthdec2 = round(stdsepallength,2)

##Print the min, max and average sepal length rounded to two decmial places
print("********************************")
print(f"The minimum sepal length is {minsepallength}")
print(f"The maximum sepal length is {maxsepallength}")
print(f"The average sepal length is {meansepallengthdec2}")
print(f"The standard devation of the sepal length is {stdsepallengthdec2}")
print("********************************")

#Assign the second column of the dataset to the array septalwidth
sepalwidth = irisdata[:,1]

#The min, max average and standard devation of the septalwidth is calculated, the mean calculation is rounded to two decimal places.
minsepalwidth = numpy.min(irisdata[:,1])
maxsepalwidth = numpy.max(irisdata[:,1])
meansepalwidth = numpy.mean(irisdata[:,1])
stdsepalwidth = numpy.std(irisdata[:,1])
meansepalwidthdec2 = round(meansepalwidth,2)
stdsepalwidthdec2 = round(stdsepalwidth,2)

#Print the min, max average and standard devation of the sepal width rounded to two decmial places
print(f"The minimum sepal width is {minsepalwidth}")
print(f"The maximum sepal width is {maxsepalwidth}")
print(f"The average sepal width is {meansepalwidthdec2}")
print(f"The standard devation of the sepal width is {stdsepalwidthdec2}")
print("********************************")

#Assign the third column of the dataset to the array septallength
petallength = irisdata[:,2]

#The min, max average and standard devation of the petallength is calculated, the mean calculation is rounded to two decimal places.
minpetallength = numpy.min(irisdata[:,2])
maxpetallength = numpy.max(irisdata[:,2])
meanpetallength = numpy.mean(irisdata[:,2])
stdpetallength = numpy.std(irisdata[:,2])
meanpetallengthdec2 = round(meanpetallength,2)
stdpetallengthdec2 = round(stdpetallength,2)

##Print the min, max average and standard devation of the petal length rounded to two decmial places
print(f"The minimum petal length is {minpetallength}")
print(f"The maximum petal length is {maxpetallength}")
print(f"The average petal length is {meanpetallengthdec2}")
print(f"The standard devation of the petal length is {stdpetallengthdec2}")
print("********************************")

#Assign the fourth column of the dataset to the array petalwidth
petalwidth = irisdata[:,3]

#The min, max average and standard devation of the petalwidth is calculated, the mean calculation is rounded to two decimal places.
minpetalwidth = numpy.min(irisdata[:,3])
maxpetalwidth = numpy.max(irisdata[:,3])
meanpetalwidth = numpy.mean(irisdata[:,3])
stdpetalwidth = numpy.std(irisdata[:,3])
meanpetalwidthdec2 = round(meanpetalwidth,2)
stdpetalwidthdec2 = round(stdpetalwidth,2)


#Print min, max average and standard devation of the sepal width rounded to two decmial places
print(f"The minimum petal width is {minpetalwidth}")
print(f"The maximum petal width is {maxpetalwidth}")
print(f"The average petal width is {meanpetalwidthdec2}")
print(f"The standard devation of the petal width is {stdpetalwidthdec2}")
print("********************************")
