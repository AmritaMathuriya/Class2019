
def recSearch (num, list1, currLen) :
    if (currLen <= 0): # base case 
        return False
    if ( num == list1[currLen-1]):
        return True
    else :
        return recSearch(num, list1, currLen-1)


list1 = [3, 100, 45, 23, 1, 9, 2]
len1 = len(list1)
num = 4 

found = recSearch( num, list1, len1)
print ("Number ", num, " found: ", found)
