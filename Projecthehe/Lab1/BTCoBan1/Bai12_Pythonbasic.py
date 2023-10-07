#12. Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.
import calendar
y = int(input("Nhập năm : "))
m = int(input("Nhập tháng : "))
print(calendar.month(y, m))