#3. Write a Python program to display the current date and time.
from datetime import datetime
from datetime import date
day= date.today()
time= datetime.now()
current_time = time.strftime("%H:%M:%S") # Phương thức strftime để định dạng hiện thị giờ ở 1 dang khác
print(f"Ngày hiện tại là {day}, giờ hiện tại là {current_time}")