
# Function to do binary search in a sorted list. 
def binary_search(list1,num):

    start = 0
    end = len(list1)-1
    found = False
    
    while( start <= end and not found): # Either start > end or you found is True. 

        midIndex = (start + end ) // 2
        print ("midIndex: ", midIndex, " start = ", start, " end = ", end)
    
        if list1[midIndex] == num :  # found the number, break the loop by making found = True
            found = True
    
        else:
            if num < list1[midIndex]: # Search number is smaller than mid point - it should reside on the left side.
                end = midIndex - 1
            else: 
                start = midIndex + 1 # Search number is greater than mid point - it should reside on the right side.

    return found


list1 = [1,2,3,5,8]
num = 5 
found = binary_search(list1, num)
print (found)

#print(binary_search([1,2,3,5,8], 5))
