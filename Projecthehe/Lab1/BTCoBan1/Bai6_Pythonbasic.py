#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')
values = input("Input some comma seprated numbers : ") # nhập vào list, cách nhau bởi dấu phẩy
list = values.split(",") # tách nhau ra bằng dấu phẩy
tuple = tuple(list) #chuyển đổi danh sách thành một bộ bằng cách sử dụng hàm tuple() và gán nó cho biến 'tuple'.
print('List : ',list)
print('Tuple : ',tuple)
