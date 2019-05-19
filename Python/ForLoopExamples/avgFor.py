# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:43:05 2019

@author: Amrita
"""

import numpy as np

N = int(input("Enter N: "))
X = np.zeros(N)

print (X)


sum = 0
for i in range (N):
    X[i] = int(input("Please enter number: "))
    sum += X[i]
    
avg = sum/N
print (avg)
    
