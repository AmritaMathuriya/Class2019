
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
str1 = fin.readline().split()
print str1

sum = 0
for i in str1 :
    sum = sum + int(i)
print sum 

fout.write (str(sum) + '\n')
fout.close()
