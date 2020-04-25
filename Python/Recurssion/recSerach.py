
def recSearch (num, start, end, list1) :
    print ( "num = ", num, " start = ", start, " end = ", end, " list1 = ", list1)
    if (start==end): # base case 
        return False
    if ( num == list1[start]):
        return True
    else :
        return recSearch(num, start+1, end, list1)


list1 = [3, 100, 45, 23, 1, 9, 2]
num = 4 

found = recSearch( num, 0, len(list1), list1)
print (found)
