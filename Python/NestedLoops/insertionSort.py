def swap (p1, p2, listC):
    temp = listC[p1]
    listC[p1] = listC[p2]
    listC[p2] = temp


def funInner (listC, lastPos):
    last = listC[lastPos]
    
    for i in range ( lastPos-1, -1, -1 ):
        if listC[i] > last : 
            swap ( i,  lastPos, listC )
            lastPos = i
    
        print (listC)
    print ("")
    return listC

list1 = [2, 5, 1, 3, 4, 10, 12, 7]
print (list1)
print ("")

len1 = len(list1)

for i in range (len1-1):
    lastPos = i+1 
    funInner(list1, lastPos)

