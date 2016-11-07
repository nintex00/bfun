# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:18:51 2016

@author: Brad
"""

import math

def euclideanDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
      distance += pow((instance1[x] - instance2[x]),2)
   return math.sqrt(distance)
   