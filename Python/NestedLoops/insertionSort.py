def swap (p1, p2, list1):
    temp = list1[p1]
    list1[p1] = list1[p2]
    list1[p2] = temp


def funInner (lastPos):
    last = list1[lastPos]
    
    for i in range ( lastPos-1, -1, -1 ):
        if list1[i] > last : 
            swap ( i,  lastPos, list1 )
            lastPos = i
    
        print (list1)
    print ("")


list1 = [2, 5, 1, 3, 4, 10, 12, 7]
len1 = len(list1)

for i in range (len1-1):
    lastPos = i+1 
    funInner(lastPos)

