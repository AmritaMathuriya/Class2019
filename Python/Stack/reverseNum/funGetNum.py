
def getNum( st ):

    reverse = 0
    place = 1
    # Popping the digits and forming 
    # the reversed number 

    while (len(st) > 0):

        elem = st.pop() 
        prevNum = reverse

        reverse = prevNum + (elem * place);
        print "elem: ", elem, " reverse: ", reverse, ", place: ", place, ", stack: ", st
        place = place * 10;

    return reverse 

st = [5, 6, 3]
print st

reverse = getNum(st)

print reverse

