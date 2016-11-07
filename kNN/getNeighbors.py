# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:31:00 2016

@author: Brad
"""

import operator
from euclideanDistance import euclideanDistance

def getNeighbors(trainingSet, testInstance, k):
   distances = []
   length = len(testInstance)-1
   for x in range(len(trainingSet)):
      dist = euclideanDistance(testInstance, trainingSet[x], length)
      distances.append((trainingSet[x],dist))
   distances.sort(key=operator.itemgetter(1))
   neighbors = []
   for x in range(k):
      neighbors.append(distances[x][0])
   return neighbors
   
