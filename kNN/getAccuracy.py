# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:05:43 2016

@author: Brad
"""

def getAccuracy(testSet, predictions):
   correct = 0
   for x in range(len(testSet)):
      if testSet[x][-1] == predictions[x]:
         correct += 1
   return(correct/float(len(testSet))) * 100.0