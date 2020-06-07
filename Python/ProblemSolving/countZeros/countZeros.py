

def fun_countZero(N, X):

    zeros = 0
    for i in X:
        if i.isdigit():
            elem = int(i)
            if elem == 0:
                zeros = zeros + 1

#    fib_N_1, list1 = fun_fib(N-1, list1) 
#    fib_N_2 = list1[len(list1)-2]
#
#    fib_N = fib_N_2 + fib_N_1
    
#    list1.append(fib_N)
    return zeros 

def main():
    fIn = open("input.txt", "r")
    fOut = open ("output.txt", "w")
    
    numTests = int(fIn.readline())
    print (numTests)

    for i in range(numTests):
        N = int( fIn.readline() )
        X = ( fIn.readline() )

        print (N, X)

        zeros = fun_countZero(N, X)


        fOut.write( str(zeros) + "\n" )

        #print(list1)

    fIn.close()
    fOut.close()


main()


