def funCount (argStr) :
    count = 0
    for x in argStr :
        count = count + 1
    return count    
    
str1 = "This is an orange."
mycount = funCount(str1)

print (str1)
print (mycount)

