import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyodbc
from tkinter import messagebox
import re

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=WINDOWS-10\SQLEXPRESS;'
                      'DATABASE=QuanLyDanhBa12;'
                      'Trusted_Connection=yes;')


def display_contacts():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Contacts')
    contacts = cursor.fetchall()
    
    for row in tree.get_children():
        tree.delete(row)
    
    for contact in contacts:
        # Xử lý dữ liệu trước khi hiển thị
        cleaned_data = [str(field).replace("'", "") for field in contact]
        tree.insert('', 'end', values=cleaned_data)

def add_contact():
    ho_ten = ho_ten_entry.get()
    dia_chi_email = dia_chi_email_entry.get()
    so_dien_thoai = so_dien_thoai_entry.get()
    dia_chi = dia_chi_entry.get()
    ngay_sinh = ngay_sinh_entry.get()

    cursor = conn.cursor()
    cursor.execute('INSERT INTO Contacts (HoTen, DiaChiEmail, SoDienThoai, DiaChi, NgaySinh) VALUES (?, ?, ?, ?, ?)',
                   (ho_ten, dia_chi_email, so_dien_thoai, dia_chi, ngay_sinh))
    conn.commit()

    ho_ten_entry.delete(0, 'end')
    dia_chi_email_entry.delete(0, 'end')
    so_dien_thoai_entry.delete(0, 'end')
    dia_chi_entry.delete(0, 'end')
    ngay_sinh_entry.delete(0, 'end')

    display_contacts()

def edit_contact():
    selected_item = tree.selection()
    if selected_item:
        selected_contact_id = tree.item(selected_item)['values'][0]
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Contacts WHERE ID = ?', (selected_contact_id,))
        contact = cursor.fetchone()
        if contact:
            ho_ten_entry.delete(0, 'end')
            dia_chi_email_entry.delete(0, 'end')
            so_dien_thoai_entry.delete(0, 'end')
            dia_chi_entry.delete(0, 'end')
            ngay_sinh_entry.delete(0, 'end')

            ho_ten_entry.insert(0, contact.HoTen)
            dia_chi_email_entry.insert(0, contact.DiaChiEmail)
            so_dien_thoai_entry.insert(0, contact.SoDienThoai)
            dia_chi_entry.insert(0, contact.DiaChi)
            ngay_sinh_entry.insert(0, contact.NgaySinh)


def save_contact():
    selected_item = tree.selection()
    if selected_item:
        selected_contact_id = tree.item(selected_item)['values'][0]
        ho_ten = ho_ten_entry.get()
        dia_chi_email = dia_chi_email_entry.get()
        so_dien_thoai = so_dien_thoai_entry.get()
        dia_chi = dia_chi_entry.get()
        ngay_sinh = ngay_sinh_entry.get()
        
        cursor = conn.cursor()
        cursor.execute('UPDATE Contacts SET HoTen=?, DiaChiEmail=?, SoDienThoai=?, DiaChi=?, NgaySinh=? WHERE ID=?',
                       (ho_ten, dia_chi_email, so_dien_thoai, dia_chi, ngay_sinh, selected_contact_id))
        conn.commit()
        
        ho_ten_entry.delete(0, 'end')
        dia_chi_email_entry.delete(0, 'end')
        so_dien_thoai_entry.delete(0, 'end')
        dia_chi_entry.delete(0, 'end')
        ngay_sinh_entry.delete(0, 'end')
        
        display_contacts()
        

def delete_contact():
    selected_item = tree.selection()
    if selected_item:
        selected_contact_id = tree.item(selected_item)['values'][0]
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Contacts WHERE ID = ?', (selected_contact_id,))
        conn.commit()
        display_contacts()



    
    
def search_contacts():
    keyword = search_entry.get()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contacts WHERE HoTen LIKE ? OR SoDienThoai LIKE ? ", ('%' + keyword + '%', '%' + keyword + '%'))
    contacts = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for contact in contacts:
        cleaned_data = [str(field).replace("'", "") for field in contact]
        tree.insert('', 'end', values=cleaned_data)

    #hàm kiểm tra email có hợp lệ không
def validate_email_input():
    email = dia_chi_email_entry.get()
    pattern = r'^\w+@\w+\.\w+$'
    if not re.match(pattern, email):
        messagebox.showerror("Lỗi", "Email không hợp lệ.")
             
    
    #hàm kiểm tra sdt có hợp lệ không
def validate_sdt_input(event):
    sdt = so_dien_thoai_entry.get()
    if not sdt.isdigit() or len(sdt) != 10:
        messagebox.showerror("Lỗi", "Số điện thoại phải chứa đúng 10 số.")
        
        # kiểm tra định dạng ngày sinh nhập vào
def validate_ngaysinh_input():
    ngaysinh = ngay_sinh_entry.get()
    pattern ='^\d{2}-\d{2}-\d{4}$'

    if not re.match(pattern, ngaysinh):
        messagebox.showerror("Lỗi", "Ngày sinh không đúng định dạng YYYY-MM-DD.")
        
if __name__=="__main__":    
    root = tk.Tk()
    root.title("Ứng dụng Quản lý danh bạ")
    root.geometry("1000x400")
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)
    root.configure(background="lightblue")


    label = ttk.Label(frame, text="Danh sách liên hệ")
    label.grid(row=0, column=0, columnspan=1, sticky="w")  # Sử dụng "sticky" để căn chỉnh sang bên trái

    tree = ttk.Treeview(frame, columns=("ID", "Họ tên", "Địa chỉ email", "Số điện thoại", "Địa chỉ", "Ngày sinh"))
    tree.grid(row=1, column=0, columnspan=6)


    tree.column("#1", width=50)  # Cột ID
    tree.column("#2", width=150)  # Cột Họ tên
    tree.column("#3", width=150)  # Cột Địa chỉ email
    tree.column("#4", width=100)  # Cột Số điện thoại
    tree.column("#5", width=150)  # Cột Địa chỉ
    tree.column("#6", width=100)  # Cột Ngày sinh

# Tiêu đề cột
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Họ tên")
    tree.heading("#3", text="Địa chỉ email")
    tree.heading("#4", text="Số điện thoại")
    tree.heading("#5", text="Địa chỉ")
    tree.heading("#6", text="Ngày sinh")
    display_contacts()

    ho_ten_label = ttk.Label(frame, text="Họ tên:")
    ho_ten_label.grid(row=2, column=0, sticky="e")
    ho_ten_entry = ttk.Entry(frame)
    ho_ten_entry.grid(row=2, column=1, sticky="w")  # Đặt sticky="w" để căn chỉnh về phía tây (west)

    dia_chi_email_label = ttk.Label(frame, text="Địa chỉ email:")
    dia_chi_email_label.grid(row=2, column=2, sticky="e")
    dia_chi_email_entry = ttk.Entry(frame)
    dia_chi_email_entry.grid(row=2, column=3, sticky="w")

    so_dien_thoai_label = ttk.Label(frame, text="Số điện thoại:")
    so_dien_thoai_label.grid(row=4, column=0, sticky="e")
    so_dien_thoai_entry = ttk.Entry(frame)
    so_dien_thoai_entry.grid(row=4, column=1, sticky="w")

    dia_chi_label = ttk.Label(frame, text="Địa chỉ:")
    dia_chi_label.grid(row=4, column=2, sticky="e")
    dia_chi_entry = ttk.Entry(frame)
    dia_chi_entry.grid(row=4, column=3, sticky="w")

    ngay_sinh_label = ttk.Label(frame, text="Ngày sinh:")
    ngay_sinh_label.grid(row=6, column=0, sticky="e")
    ngay_sinh_entry = ttk.Entry(frame)
    ngay_sinh_entry.grid(row=6, column=1, sticky="w")

    search_entry = ttk.Entry(frame)
    search_entry.grid(row=0, column=4,sticky="w")
    search_button = ttk.Button(frame, text="Tìm kiếm", command=search_contacts)
    search_button.grid(row=0, column=5)

    add_button = ttk.Button(frame, text="Thêm liên hệ", command=add_contact)
    add_button.grid(row=11, column=2)

    edit_button = ttk.Button(frame, text="Sửa liên hệ", command=edit_contact)
    edit_button.grid(row=11, column=3)

    # Nút "Lưu liên hệ"
    save_button = ttk.Button(frame, text="Lưu liên hệ", command=save_contact)
    save_button.grid(row=11, column=4)

    delete_button= ttk.Button(frame, text="Xoá", command=delete_contact)
    delete_button.grid(row=11, column=5)

    # kiểm tra xem nhập đúng mã số sinh viên, email, số điện thoại, học kỳ, ngày sinh thông qua các hàm đã tạo trước đó
    
    dia_chi_email_entry.bind("<FocusOut>", lambda e: validate_email_input())
    so_dien_thoai_entry.bind("<FocusOut>", validate_sdt_input)
    ngay_sinh_entry.bind("<FocusOut>", lambda e: validate_ngaysinh_input())


root.mainloop()