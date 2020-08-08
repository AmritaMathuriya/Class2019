numberList = [3, 1, 21, 4, 65, 7, 43, 8]
print (numberList)
num = len(numberList) 

i = 0
while(i < num):
    x = i + 1
    while(x < num):

        # compare and swap, if number at i is greater than number at x
        if(numberList[i] > numberList[x]):
            print ("Switching: ", numberList[i],  numberList[x])
            temp = numberList[i]
            numberList[i] = numberList[x]
            numberList[x] = temp            
        print( "i=", i, " x=", x, numberList)
        x = x + 1

    print ("")
    i = i + 1


print(numberList)

