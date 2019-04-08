
st1 = "This is an orange"

len = len(st1)

print (len)


words = []
word = []

for i in range (len):
    if ( st1[i] != ' '):
        word.append(st1[i])
    else: 
        words.append(word)
        word = []


print (words)
