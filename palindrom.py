# Python code to check if a string is palindrome or not

def isPalindrom(s):
    return s==s[::-1]

# Driver code
s = input("Enter a string: ")
ans = isPalindrom(s)

if ans:
    print("{0} is a Palindrom".format(s))
else:
    print("{0} is not a Palindrom".format(s))

# m = "namaga"
# n = m[::-1]
# print(n)