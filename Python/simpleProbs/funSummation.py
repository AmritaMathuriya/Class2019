
def add(end1):
    print(end1)
    #print(a)
    sum = 0
    for i in range(1, end1+1):
        sum = sum + i
    #print(sum)
    return sum
end = input("Please enter number: ")
end = int(end)

a = add(end)
b = add(4)
print(a)
print(b)
