list1 = [2, 4, 3, 4, 1, 2 , 1, 0, 1, 1]
len1 = len(list1)

import numpy
freq = numpy.zeros(5, int)
print freq

for i in range (len1):
    c = list1 [i]
    freq[c] = freq[c] + 1

print freq
list2 = []
for i in range (len(freq)):
    for j in range (freq[i]) :
        list2.append(i)

print list1
print list2
