# Python program to calculate sum of the digits of number
def sumOfDigits(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

        
    print(sum)

num = int(input("Enter the number: "))
sumOfDigits(num)