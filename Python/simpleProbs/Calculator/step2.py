
a = input ("Feed the first number: ")
b = input ("Feed the second number: ")
a = int(a)
b = int(b)

ans = -1

option = input("Please enter add/sub/mult/div: ")
if option == "add": 
    ans = a + b 

if option == "sub":
    ans = a - b

if option == "mult":
    ans = a * b

if option == "div":
    ans = a / b


print (ans)

