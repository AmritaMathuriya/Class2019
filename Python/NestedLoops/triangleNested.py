N = 5 

print "Outer loop dimension: ", N 

for i in range(N):
    list1 = []
    for j in range (i+1):
        list1.append(j)
    print list1 
