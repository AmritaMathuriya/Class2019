list1 = [24, 4, 56, 18, 32, 6, 12, 7, 213, 5]
print(len(list1))
print ("")

def whileloop(j):

    if j == 0: 
        return

    whileloop(j-1)
    current = list1[j]
    i = j

    while i >= 1 and current < list1[i - 1]:
        list1[i] = list1[i - 1]
        i = i - 1
    list1[i] = current

    return




def insertionsort():
    whileloop(len(list1)-1)

insertionsort()

print(list1)
