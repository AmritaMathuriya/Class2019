
def add ( a, b ):
    return a + b

def sub ( a, b ):
    return a - b

def mult ( a, b ):
    return a * b

def div ( a, b ):
    return a / b

def main ()
    while ( True ):
        a = input ("Feed the first number: ")
        b = input ("Feed the second number: ")
        a = int(a)
        b = int(b)
        
        ans = -1
        
        option = input("Please enter add/sub/mult/div: ")
        if option == "add": 
            ans = add (a,b)
        
        if option == "sub":
            ans = sub(a,b)
        
        if option == "mult":
            ans = mult(a,b)
        
        if option == "div":
            ans = div(a,b)    
        
        print ("Answer is: ", ans)
        TryAgain = input("Try again yes/no? : ")
        if TryAgain == "no" : 
            break
    
        
