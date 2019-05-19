# Problem2: Remove duplicates (if any exist) from a sorted array. 
# Level of difficulty: Medium. Reasonably easy. 
# Hint: Please note that the array is sorted. 
# Input: [1, 4, 4, 5, 9, 9, 100 ]
# Output: [ 1, 4, 5, 9, 100]

myList = [ 7, 9, 9, 9, 12, 13, 13, 100,100, 100 ]
print "Input: ", myList
myList.append(10^9)

len1 = len(myList)
print "length of the array : ", len1-1


un1 = []
for i in range ( len1 - 1 ):
    c = myList[i]
    n = myList[i+1]

    if ( c != n ):
        un1.append ( c )

#un1.append( myList [ len1-1 ])

print "Unique elements:", un1
