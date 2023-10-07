#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
n=int(input("Nhap n: "))
print(f"{n} nam trong pham vi 100 cua 1000 hoac 2000") if ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)) else print(f"{n} nam ngoai pham vi 100 cua 1000 hoac 2000")