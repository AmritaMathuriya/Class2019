sentence = "my name is hello"
len1 = len(sentence)


count = 0
pos = []
for i in range (len1):
    if sentence[i] == 'e':
        count = count+1
        pos.append(i)

print (count, pos)

