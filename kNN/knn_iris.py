# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:23:27 2016

@author: Brad
"""

import numpy as np
import matplotlib.pyplot as plt

import csv
from loadDataset import loadDataset
from getNeighbors import getNeighbors
from getResponse import getResponse
from getAccuracy import getAccuracy

with open(r'C:\Users\Brad\Documents\GIT\bfun\kNN\iris_2_classes.data', 'r') as csvfile:
   lines = csv.reader(csvfile)
   for row in lines:
      print(', '.join(row))


#### KNN 

# prepare data
trainingSet=[]
testSet=[]
split = 0.67
#loadDataset('iris_2_classes.data', split, trainingSet, testSet)
loadDataset('iris.data', split, trainingSet, testSet)
print('Train set: ' + repr(len(trainingSet)))
print('Test set: ' + repr(len(testSet)))

# generate predictions
predictions=[]
k = 3
for x in range(len(testSet)):
   neighbors = getNeighbors(trainingSet, testSet[x], k)
   result = getResponse(neighbors)
   predictions.append(result)
   print('> predicted=' + repr(result) + ', actual =' + repr(testSet[x][-1]))
accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')


