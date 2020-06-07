

def fun_countZero(var1, var2):

    print (var1, var2)
    zeros = 0
    for i in var2:
        if i.isdigit():
            elem = int(i)
            if elem == 0:
                zeros = zeros + 1

    return zeros 

def main():
    fIn = open("input.txt", "r")
    fOut = open ("output.txt", "w")
    
    numTests = int(fIn.readline())
    print (numTests)

    for i in range(numTests):
        N = int( fIn.readline() )
        X = ( fIn.readline() )

        zeros = fun_countZero(N, X)
        fOut.write( str(zeros) + "\n" )

    fIn.close()
    fOut.close()


main()


