# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 21:59:07 2016

@author: Clark
"""



# Example of kNN implemented from Scratch in Python
 
import csv
import random
import operator
from loadDataset import loadDataset

# prepare data
trainingSet=[]
testSet=[]
split = 0.67
loadDataset('iris.data', split, trainingSet, testSet)
print('Train set: ' + repr(len(trainingSet)))
print('Test set: ' + repr(len(testSet)))

predictions=[]
k = 3
for x2 in range(len(testSet)):
    testInstance=testSet[x2]
    distances = []
    length = len(testInstance)-1
    for x3 in range(len(trainingSet)):
        instance1=testInstance
        instance2=trainingSet[x3]
        distance = 0
        for x4 in range(length):
            distance += pow((instance1[x4] - instance2[x4]), 2)
        dist=distance
        distances.append((trainingSet[x3], dist))        
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x5 in range(k):
        neighbors.append(distances[x5][0])
    classVotes = {}
    for x6 in range(len(neighbors)):
        response = neighbors[x6][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    result=sortedVotes[0][0]
 
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x2][-1]))
    
correct = 0
for x7 in range(len(testSet)):
    if testSet[x7][-1] == predictions[x7]:
        correct += 1
accuracy = (correct/float(len(testSet))) * 100.0
 	
print('Accuracy: ' + repr(accuracy) + '%')
