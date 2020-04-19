num = input("Enter number: ")
num = int(num)

def fun1 ( x ):
    if x == 1:
        return 1
    else: 
        return (1.0/x) + fun1(x-1)

sum1 = fun1(num)
print sum1
