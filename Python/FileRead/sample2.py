fin = open ('test.in', 'r')
fout = open ('test.out', 'w')

str1 = fin.readline()
print str1

str2 = str1.split()
print str2

x = int(str2[0])
y = int(str2[1])

z = x + y
print z

#x,y = fin.readline().split()
#sum = x+y
fout.write (str(sum) + '\n')
fout.close()
