#Write a Python program to calculate the number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days
from datetime import date
def XuLy(ngaybd:date, ngaykt:date):
    kq = ngaykt - ngaybd
    return kq
ngaybd= date(2014, 7, 2)
ngaykt =date(2014, 7, 11)
kq = XuLy(ngaybd, ngaykt)
print(f"Kết quả là: {kq.days}")
