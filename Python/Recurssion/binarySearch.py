
def binary_search(list1,num):

    start = 0
    end = len(list1)-1
    found = False
    
    while( start <= end and not found): # Either start > end or you found is True. 

        midIndex = (start + end ) // 2
        print ("midIndex: ", midIndex, " start = ", start, " end = ", end)
    
        if list1[midIndex] == num :
            found = True
    
        else:
            if num < list1[midIndex]:
                end = midIndex - 1
            else: 
                start = midIndex + 1

    return found


list1 = [1,2,3,5,8]
num = 5 
found = binary_search(list1, num)
print (found)

#print(binary_search([1,2,3,5,8], 5))
