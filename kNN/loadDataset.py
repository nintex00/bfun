# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:00:55 2016

@author: Brad
"""

import csv
import random

def loadDataset(filename, split, trainingSet=[], testSet=[]):
   with open(filename, 'r') as csvfile:
      lines = csv.reader(csvfile)
      dataset = list(lines)
      for x in range(len(dataset) -1):
         for y in range(4):
            dataset[x][y] = float(dataset[x][y])
         if random.random() < split:
            trainingSet.append(dataset[x])
         else:
            testSet.append(dataset[x])