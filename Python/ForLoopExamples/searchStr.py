st1 = "This is an orange "

words = st1.split()
len1 = len(words)

s_word = "is"
foundIt = False

for i in range ( len1 ):
    if s_word == words[i]:
        print "Found it at: ", i, " ", words[i]
        foundIt = True

if foundIt == False:
    print "Couldn't find it."

