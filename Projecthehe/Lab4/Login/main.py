import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Login")
root.geometry("250x300")
root.resizable(False,False)
root.configure(bg="#fff")

name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password = passw_var.get()
    print("The name is: " + name)
    print("The password is: " +password)


# tạo label hiển thị mục username
Label(root,text="Username", font=('calibre',10, 'bold')).place(x=0, y=0) # vùng hiển thị, x = ô = 0, y = hàng = 0 (Sát trên và sát trái)
# tạo label hiển thị mục password
Label(root,text="Password", font=('calibre',10, 'bold')).place(x=0, y=30) # vùng hiển thị, x = ô = 0, y = hàng = 30 (sát trái, cách trên 30)
# tạo ô để nhập username, biến lưu vào name_var
Entry(root, textvariable= name_var, font = ('calibre',10,'normal')).place(x=80, y=0) # cách trái 80, sát trên
# tạo ô để nhập password, biến lưu vào passw_var, hiện thị '*'
Entry(root, textvariable= passw_var, font = ('calibre',10,'normal'), show='*').place(x=80, y=30) # cách trái 80, cách trên 30
# tạo nút submit
Button(root, text="Submit",font=("arial",11, "bold"),bd=1, fg="#fff",bg="#2a2d36",command=submit).place(x=90, y=90)








root.mainloop()