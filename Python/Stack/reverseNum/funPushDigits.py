

def push_digits(number):

    while (number != 0):
        remainder = number % 10
        dividend = number / 10
        print "number: ", number, "remainder: ", remainder, "dividend:", dividend

        st.append(remainder);
        number = int(dividend);
    print number

st = []
num = 365 
push_digits(num)

print ""

print num 
print st
