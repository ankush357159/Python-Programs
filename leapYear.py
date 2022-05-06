# Python code to check wether a year is a leap year or not
# If a year is divisible by 400 then it is a leap year
# If a year is divisible by 4 and 100, then it is a leap year
# Else not a leap year

# Method 1
def checkYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Method 2
def leapYear(year):
    if ((year % 4) == 0 and (year % 100) == 0):
        return True
    elif (year % 400) == 0:
        return True
    else:
        return False

  


year = int(input("Enter a year: "))

# if checkYear(year):
#     print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))


if leapYear(year):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
	