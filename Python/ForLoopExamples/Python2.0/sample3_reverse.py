import sys

N = input("Please input N: ") 
for i in range(N):
    for j in range(N-i):
        sys.stdout.write('x')
    print("")
