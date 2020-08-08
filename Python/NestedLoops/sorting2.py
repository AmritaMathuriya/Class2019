numberList = [3, 1, 21, 4, 65, 7, 43, 8]
print (numberList)
num = len(numberList) 

for i in range (0,num):
    for x in range (i+1, num):

        # compare and swap, if number at i is greater than number at x
        if(numberList[i] > numberList[x]):
            print ("Switching: ", numberList[i],  numberList[x])
            temp = numberList[i]
            numberList[i] = numberList[x]
            numberList[x] = temp            
        print( "i=", i, " x=", x, numberList)

    print ("")


print(numberList)

