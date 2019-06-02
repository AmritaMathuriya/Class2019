#Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#1) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#3) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

list1 = [100, 20, 3, 6, 1, 9]
list2 = []
num = input("Please input the threshold number: ")
for i in list1 :
    if i < num:
        list2.append(i)

print list2

