

def fun_fib(N, list1):
    if ( N <= 2 ):
        return 1, list1

    fib_N_1, list1 = fun_fib(N-1, list1) 
    fib_N_2 = list1[len(list1)-2]

    fib_N = fib_N_2 + fib_N_1
    
    list1.append(fib_N)
    return fib_N, list1 

def main():
    fIn = open("input.txt", "r")
    fOut = open ("output.txt", "w")
    
    numTests = int(fIn.readline())
    print (numTests)

    for i in range(numTests):
        N = int( fIn.readline() )
        print (N)

        list1 = [1, 1]
        fib_N, list1 = fun_fib(N, list1)


        fOut.write( str(list1) + "\n" )

        #print(list1)

    fIn.close()
    fOut.close()


main()


