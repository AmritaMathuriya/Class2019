
def fun1(myList):
    print (myList)
    sumList = 0
    for i in range ( len (myList) ):
        sumList = sumList + myList[i]

    return sumList

arr1 =  [3, 1, 2 ]

sum1 = fun1(arr1)
print (sum1)

arr2 = [1, 4, 2]
sum2 = fun1(arr2)
print (sum2)
