fIn = open("input.txt", "r")
fOut = open ("output.txt", "w")

numTests = int(fIn.readline())
print (numTests)

def fun_fib(N, list1):
    if ( N == 2 or N == 1 ):
        return 1, list1

    fib_N_1, list1 = fun_fib(N-1, list1) 
    fib_N = list1[len(list1)-2] + fib_N_1
    
    list1.append(fib_N)
    return fib_N, list1 

for i in range(numTests):
    N = int( fIn.readline() )
    list1 = [1, 1]
    fib_N, list1 = fun_fib(N, list1)
    fOut.write(str(list1))
    fOut.write("\n")
    print(list1)

fIn.close()
fOut.close()



#N = 2
#print (fun_fib(N))

