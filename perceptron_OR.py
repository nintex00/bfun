# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:47:56 2016

@author: Brad
"""

import numpy as np
import matplotlib.pyplot as plt

input = np.matrix('0 0; 0 1; 1 0; 1 1')
numIn = 4
desired_out = np.matrix('0; 1; 1; 1')
bias = -1 
coeff = 0.7 # learning rate
weights = -1*2*np.random.rand(3,1)

iterations = 1000
rms_err= np.zeros(iterations)

for i in range(iterations):
   out = np.zeros(4)
   
   for j in range(numIn):
      y = bias*weights[0][0] + input[j,0]*weights[1][0] + input[j,1]*weights[2][0]
      out[j] = 1 / (1+np.exp(-y))
      delta = desired_out[j] - out[j] # delta rule, levenberg-marquardt could be used
      weights[0][0] = weights[0][0] + coeff*bias*delta
      weights[1][0] = weights[1][0] + coeff*input[j,0]*delta
      weights[2][0] = weights[2][0] + coeff*input[j,1]*delta
   
   sum_rms = 0
   for k in range(numIn):
      sum_rms = np.power((out[k] - desired_out[k]),2) + sum_rms
   
   rms_err[i] = np.sqrt(sum_rms / len(out))


print(out)
print(weights)

plt.figure
plt.plot(range(iterations),rms_err)
plt.title("RMSE vs. Iterations")
plt.show()