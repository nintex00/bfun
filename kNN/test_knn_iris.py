# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:23:27 2016

@author: Brad
"""

import numpy as np
import matplotlib.pyplot as plt

import csv
from loadDataset import loadDataset
from euclideanDistance import euclideanDistance
from getNeighbors import getNeighbors
from getResponse import getResponse
from getAccuracy import getAccuracy

with open(r'C:\Users\Brad\Documents\GIT\bfun\iris_2_classes.data', 'r') as csvfile:
   lines = csv.reader(csvfile)
   for row in lines:
      print(', '.join(row))

## Handle data: split training data to testing data ratio = 67/33
trainingSet=[]
testSet=[]
loadDataset('iris_2_classes.data', 0.66, trainingSet, testSet)
print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))

## Similarity using Euclidean Distance
data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print('Distance: ' + repr(distance))

## Neighbors
trainSet = [[2, 2, 'a'], [4, 4,'b']]
testInstance = [5, 5, 5]
k = 1
neighbors = getNeighbors(trainSet, testInstance, k)
print(neighbors)

## Response
neighbors = [[1, 1, 1, 'a'], [2, 2, 'a'], [3, 3, 3, 'b']]
response = getResponse(neighbors)
print(response)


## Accuracy
testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)