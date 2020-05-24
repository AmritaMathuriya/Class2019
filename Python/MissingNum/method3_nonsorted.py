
arr = [1, 2, 3, 4, 6, 7, 8]
n = len(arr)+1

arr = sorted(arr)

for i in range(1, n):
    if i != arr[i-1]:
        print (i)
        break
