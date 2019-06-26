## By Aarohi

word = "racecar"
wordlist = list(word)
print wordlist
palindrome = 1

while len(wordlist) > 0:
    if len(wordlist) > 1:
        first = wordlist.pop(0)
        last = wordlist.pop()
        print first
        print last
        if first != last:
            print ("Not a palindrome!")
            palindrome = 0
            break
    else:
        break

if palindrome:
    print ("Palindrome!")
print wordlist
