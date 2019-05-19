#Written by Aarohi

import numpy as np
N = input("Input size of set: ")
x = np.zeros(N)
print x
for i in range (N) :
    x[i] = input ("Enter number: ")
print x
even_odd = []
for i in range (N) :
    if (x[i] % 2):
        even_odd.append("odd")
    else:
        even_odd.append("even")
print even_odd
