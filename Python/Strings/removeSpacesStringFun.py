def removeSpaces (argStr) :
    len1 = len(argStr)
    outStr1 = ""
    for i in range (len1) :
        if str1[i] != " ": 
            outStr1 = outStr1 + argStr[i]
    return outStr1

str1 = "This is an orange."
myOutStr1 = removeSpaces(str1)

print (str1)
print (myOutStr1)
