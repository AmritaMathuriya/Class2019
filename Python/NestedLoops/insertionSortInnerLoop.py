def swap (p1, p2, list1):
    temp = list1[p1]
    list1[p1] = list1[p2]
    list1[p2] = temp

list1 = [2, 3, 4, 10, 12, 5]
len1 = len(list1)


last = list1[len1-1]
lastPos = len1-1


print (list1)
print ("")

for i in range ( len1-2, -1, -1 ):
    if list1[i] > last : 
        swap ( i,  lastPos, list1 )
        lastPos = i
    print (list1)


print (list1)

