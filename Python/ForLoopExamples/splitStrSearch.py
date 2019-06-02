
st1 = "This is an orange"

len1 = len(st1)

print (len1)


words = []
word = []

for i in range (len1):
    if ( st1[i] != ' '):
        word.append(st1[i])
    else: 
        words.append(word)
        word = []

words.append(word)


print (words)

searchWord = "is"

print "word to search: ", searchWord
for y in words:
    z = ''.join(y)

    if z  == searchWord:
        print "Found it: ", searchWord


