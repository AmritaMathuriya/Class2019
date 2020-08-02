
sum = 0
for i in range (1, 101):
    sum = sum + i

print sum


def funSum(N):
    if N == 1:
        return 1
    else: 
        return N + funSum(N-1)

print funSum(100)


