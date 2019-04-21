# Problem2: Remove duplicates (if any exist) from a sorted array. 
# Level of difficulty: Medium. Reasonably easy. 
# Hint: Please note that the array is sorted. 
# Input: [1, 4, 4, 5, 9, 9, 100 ]
# Output: [ 1, 4, 5, 9, 100]

myList = [ 7, 9, 9, 12, 13, 13, 100 ]
print "Input: ", myList

len1 = len(myList)
print "length of the array : ", len1

un1 = []
for i in range ( len1 - 1 ):
    c = myList[i]
    n = myList[i+1]

    if ( c != n ):
        un1.append ( c )

print "Unique elements:", un1
