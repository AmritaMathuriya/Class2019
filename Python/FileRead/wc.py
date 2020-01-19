fileName = "in.txt"

file = open ( fileName, "r" )

data = file.readlines()

print data

numWords = 0
numLines = 0
numChars = 0
for line in data:
    numLines += 1
    #print line
    words = line.split()
    numWords += len(words)
    for word in words:
        numChars += len(word)

print "Number of lines: ", numLines    
print "Number of words: ", numWords
print "Number of characters: ", numChars
