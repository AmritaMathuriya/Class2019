
num = input( "Enter number: ")
num = int(num)

def funFactorial(N):
    if N == 1:
        return 1
    else:
        return N * funFactorial (N-1)

print funFactorial(num)
