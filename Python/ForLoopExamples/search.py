import numpy as np
N = int(input("Input size of set: "))
x = np.zeros(N)
print (x)
for i in range (N) :
    x[i] = int(input ("Enter number: "))
y = int(input ("Input number to search:"))
a = 0
for i in range (N) :
    if y == x[i]:
        print ("Found")
        print (i)
        print (x[i])
        a = a+1

if a == 0:
    print (y, " is not found")
    
print ("Number of times found: ", a)
