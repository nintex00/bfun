# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:50:29 2016

@author: Brad
"""

import operator

def getResponse(neighbors):
   classVotes = {}
   for x in range(len(neighbors)):
      response = neighbors[x][-1]
      if response in classVotes:
         classVotes[response] += 1
      else:
         classVotes[response] = 1
      sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse=True)
      return sortedVotes[0][0]

