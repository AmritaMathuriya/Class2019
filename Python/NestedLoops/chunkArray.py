list1 = [3,4,5, 8,9,1,8, 3,6,7]
N = 3
list3 = []
c = 0
for i in range (len(list1)/N):
    list2 = []
    for j in range (N):
        list2.append(list1[c])
        c = c+1
    list3.append(list2)

print list1
print list3


