fileName = "in1.txt"
outFile = "out1.txt"
fileIn = open ( fileName, "r" )
fileOut = open ( outFile, "w" )

data = fileIn.readlines()


words = []
for line in data:
    word = line.rstrip()
    words.append(word)

words.sort()

for word in words:
    fileOut.write(word + "\n")

fileOut.close()
fileIn.close()

