list1 = [50, 25, 1, 3, 2, 9]
len1 = len(list1)

print list1
for i in range ( len1 ):
    a = max ( list1 [0:len1-i] ) 
    pos = list1.index(a)
    print a, pos
    temp = list1[pos]
    list1[pos] = list1 [len1-i-1]
    list1[len1-i-1] = temp

print list1



#ifor i in range(len1):
#    a = 
