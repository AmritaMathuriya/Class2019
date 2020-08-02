def fun1(myList):
    print (myList)
    sumList = 0
    for i in range ( len (myList) ):
        sumList = sumList + myList[i]

    return sumList

arr = [1, 2, 3, 4, 6, 7, 8]
sum1 = fun1(arr)
print (sum1)

sum2 = 0
n = len(arr) + 1
for i in range (1, n+1):
    sum2 = sum2 + i

print (sum1, sum2, sum2-sum1)


