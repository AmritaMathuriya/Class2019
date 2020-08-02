
n = [45, 21, 19, 1, 32, 12]
len1 = len(n)

print (n)
print ("")

for i in range ( 0, len1-1 ) : 
    for x in range ( i+1, len1 ) :
        print("i=", i, " n[i]=", n[i], " n[x]= ", n[x], " x=", x, "    ", n)
        if n[i] > n[x] :
            temp = n[i]
            n[i] = n[x]
            n[x] = temp
        
    print("")

print (n)
