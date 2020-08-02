
arr = [1, 2, 3, 4, 6, 7, 8]
len1 = len(arr)
n = len1 + 1

arrBool = [False] * (n+1)
print (arrBool)

for i in range (len1):
    curr = arr[i]
    arrBool[curr] = True


print (arrBool)
    

