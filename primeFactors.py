def primeNumber(num):
    c = 2
    while(num > 1):
        if (num % c == 0):
            print(c, end=" ")
            num = num / c
        
        else:
            c = c + 1
        

number = int(input("Enter the number for calculating prime factors: "))
primeNumber(number)