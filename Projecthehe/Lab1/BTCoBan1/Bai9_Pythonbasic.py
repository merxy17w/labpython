#9. Write a Python program to display the examination schedule. (extract the date from exam_s
#exam_st_date).exam_st_date = (11, 12, 2014) Sample Output : The examination will start from : 11 / 12 / 2014
from datetime import date
day = (11,12,2014) # nhập vào số nguyên ngày, tháng, năm
print( "Thời gian thi bắt đầu từ ngày: %i / %i / %i"%day) # Xuất định dạng ngày/tháng/năm, %i được sử dụng để định dạng các số nguyên.