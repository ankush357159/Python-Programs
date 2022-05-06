# Python code to check if a string is palindrome or not

def isPalindrom(s):
    return s==s[::-1]

s = "madam"
ans = isPalindrom(s)

if ans:
    print("String is Palindrom")
else:
    print("String is not a Palindrom")

m = "namaga"
n = m[::-1]
print(n)