
list1 = [ 4, 5, 7, 8, 10, 15, 68, 90, 120 ]
list2 = [5, 15, 68, 90, 100, 110]

len1 = len(list1)
len2 = len(list2)

for i in range(len1):
        dups = []
        j = 0
        while j < len2 and list1[i] != list2[j]: 
           j = j+1

        while j < len2 and list1[i] == list2[j]:
            dups.append(list2[j])
            j = j+1
            i = i+1
            #print j 
        
        if len( dups ) > 0:
            print dups     

