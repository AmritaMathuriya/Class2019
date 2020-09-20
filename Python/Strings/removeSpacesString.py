str1 = "This is an orange."
len1 = len(str1)

outStr1 = ""
for i in range (len1) :
    if str1[i] != " ": 
        outStr1 = outStr1 + str1[i]

print (str1)
print (outStr1)
