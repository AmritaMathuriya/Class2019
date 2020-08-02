st = []

num = int(input("Enter number: "))

for i in range (1, num+1 ):
    st.append(i)

fact = 1
while ( len( st ) > 0 ):
    print st
    temp = st.pop()
    fact = fact * temp


print fact
