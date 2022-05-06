# Python program to calculate sum of the digits of number
def sumOfDigits(num1, num2):
    for number in range(num1, num2 +1):

        temp = number
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum += digit
            temp //= 10

        
        print("Sum of the digits of {0} is {1} ".format(number, sum))

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
sumOfDigits(num1, num2)