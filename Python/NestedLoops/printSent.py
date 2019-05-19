
st1 = "This is an orange "
words = st1.split()
print words
len1 = len(words)
print len1

for i in range(len1) :
    str = ""
    for j in range(i+1):
        str = str + words[j] + " "
    print str
