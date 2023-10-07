#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference
def KiemTra(n):
    return (17-n) if n<=17 else ((n-17)*2)
print(KiemTra(14))
print(KiemTra(22))
