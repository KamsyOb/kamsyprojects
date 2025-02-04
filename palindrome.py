def ispalindrome(s):
    return s == s[::-1]

def stringconverter(s):
    return list(s)

s = (input("Enter a number: "))
s = stringconverter(s)

if ispalindrome(s):
    print("This is a palindrome")
else:
    print("This is not a palindrome")