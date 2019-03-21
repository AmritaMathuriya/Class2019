import sys
N = input("Please input N: ")

var = ""
for i in range(N):
    var = str(i) + " " + var
#    sys.stdout.write( str(i) + " "  ) 

print (var)
