
num1 = input("Enter number: ")

def fun1 ( num  ):
    fact = 1
    while ( num >= 1 ):
        fact = fact * num
        num = num-1
    return fact

print fun1(num1) 


