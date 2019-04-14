
list1 = [ 11, 10, 13, 7, 12, 15]
len1 = len(list1)

for i in range(len(list1)):

    if i > 0 and i < len1-1: 
        p = list1[i-1]
        c = list1[i]
        n = list1[i+1]
        if c >  p and c > n:
            print (p, c, n)
    elif i == len1-1:
        p = list1[i-1]
        c = list1[i]
        if c >  p : 
            print (p, c )

    elif i == 0:
        c = list1[i]
        n = list1[i+1]
        if c > n : 
            print (c, n )

