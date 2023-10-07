#7. Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java
filename = input("Nhập vào filename: ") # Nhập vào filename có 2 phần, ví dụ: facebook.com
f_extns = filename.split(".") #sử dụng phương thức chuỗi split() để chia giá trị của "filename" cho "."(dot) và gán kết quả cho biến "f_extns".
print ("Phần mở rộng của tệp là : " + repr(f_extns[-1])) #  -1 là phần  tử cuối, -2 là phàn tử tiếp theo,...
