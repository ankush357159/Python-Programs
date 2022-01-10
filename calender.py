import calendar

# yy = 2022
# mm = 1

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

#display calender
print("Calender:")
print(calendar.month(yy,mm))