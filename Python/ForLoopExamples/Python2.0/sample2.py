import sys

N = input("Please input N: ") 
for i in range(N+1):
    for j in range(i):
        sys.stdout.write('x')
    print("")
