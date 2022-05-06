# Python program to print prime numbers from a range of lower and upper values
def primeNumbers(lower_value, upper_value):
    for num in range(lower_value, upper_value + 1):
        if num > 1:
            for i in range (2, num):
                if ((num % i) == 0):
                    break
            else:
                print(num)


num1 = int(input("Enter lower value of the numbers: "))
num2 = int(input("Enter higher value of the numbers"))
primeNumbers(num1, num2)





