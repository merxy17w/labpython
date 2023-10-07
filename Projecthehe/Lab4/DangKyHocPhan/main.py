from openpyxl import *
from tkinter import *
from tkinter import ttk
import re
from openpyxl import Workbook
import tkinter
from tkinter import messagebox
# kiểm tra điều kiện mã số sinh viên
def validate_mssv_input(event):
    mssv = mssv_field.get()
    if not mssv.isdigit() or len(mssv) != 7:
        messagebox.showerror("Lỗi", "MSSV phải chứa đúng 7 số.")
        mssv_field.delete(0, "end")  # Xóa nội dung nhập sai
# kiểm tra email nhập vào
def validate_email_input():
    email = email_field.get()
    pattern = r'^\w+@\w+\.\w+$'
    if not re.match(pattern, email):
        messagebox.showerror("Lỗi", "Email không hợp lệ.")
        email_field.delete(0, "end")
# kiểm tra số điện thoại nhập vào
def validate_sdt_input(event):
    sdt = sdt_field.get()
    if not sdt.isdigit() or len(sdt) != 10:
        messagebox.showerror("Lỗi", "Số điện thoại phải chứa đúng 10 số.")
        sdt_field.delete(0, "end")
# kiểm tra học kỳ nhập vào đúng hay chưa
def validate_hocky_input(event):
    hocky = hocky_field.get()
    if hocky not in ["1", "2", "3"]:
        messagebox.showerror("Lỗi", "Học kỳ phải là 1, 2 hoặc 3.")
        hocky_field.delete(0, "end")
# kiểm tra định dạng ngày sinh nhập vào
def validate_ngaysinh_input():
    ngaysinh = ngaysinh_field.get()
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if not re.match(pattern, ngaysinh):
        messagebox.showerror("Lỗi", "Ngày sinh không đúng định dạng dd/mm/yyyy.")
        ngaysinh_field.delete(0, "end")
# nút gửi
def submit():
    mssv = mssv_field.get()
    hoten = hoten_field.get()
    ngaysinh = ngaysinh_field.get()
    email = email_field.get()
    sdt = sdt_field.get()
    hocky = hocky_field.get()
    namhoc = namhoc_field.get()

    # Kiểm tra xem có chọn ít nhất một môn học hay không
    if not var1.get() and not var2.get() and not var3.get() and not var4.get():
        messagebox.showerror("Lỗi", "Vui lòng chọn ít nhất một môn học.")
        return

    # Kiểm tra điều kiện về mã số sinh viên, email, số điện thoại, học kỳ, và ngày sinh
    if (
        not mssv or len(mssv) != 7 or not mssv.isdigit() or
        not re.match(r'^\w+@\w+\.\w+$', email) or
        not sdt.isdigit() or len(sdt) != 10 or
        hocky not in ["1", "2", "3"] or
        not re.match(r'^\d{2}/\d{2}/\d{4}$', ngaysinh)
    ):
        messagebox.showerror("Lỗi", "Vui lòng kiểm tra lại thông tin.")
        return

    # Tạo một Workbook mới và lựa chọn một sheet (hoặc tạo một sheet mới)
    wb = Workbook()
    sheet = wb.active

    # Thêm thông tin vào các cột
    sheet.append(["Mã số sinh viên", "Họ tên", "Ngày sinh", "Email", "Số điện thoại", "Học kỳ", "Năm học", "Môn học"])

    # Điền thông tin của sinh viên
    selected_courses = []
    if var1.get():
        selected_courses.append("Lập trình Python")
    if var2.get():
        selected_courses.append("Lập trình Java")
    if var3.get():
        selected_courses.append("Công nghệ phần mềm")
    if var4.get():
        selected_courses.append("Phát triển ứng dụng web")

    sheet.append([mssv, hoten, ngaysinh, email, sdt, hocky, namhoc, ", ".join(selected_courses)])

    # Lưu tập tin Excel
    wb.save(r'D:/python/Projecthehe/Lab4/DangKyHocPhan/hocphan.xlsx')

    messagebox.showinfo("Thông báo", "Đăng ký thành công.")
if __name__=="__main__":
   
    root = Tk()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    # set màu nền cho cửa sổ
    root.configure(background='light green')
 
    # set tên của chương trình
    root.title("Đăng ký học phần")
 
    # set giá trị cửa sổ là 500 x 300
    root.geometry("800x300")
    # tạo 1 heading "THÔNG TIN ĐĂNG KÝ HỌC PHẦN", background, màu chữ, vị trí xuất hiện, font, size, kiểu chữ
    heading = Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", bg="light green", fg="red", font=("Arial", 15, "bold")).place(x=120, y=5)

    mssv = Label(root, text="Mã số sinh viên", bg="light green").place(x=10, y=30)
 
    # tạo label "Họ tên"
    hoten = Label(root, text="Họ tên", bg="light green").place(x=10, y=50)
 
    # tạo label "ngày sinh"
    ngaysinh = Label(root, text="Ngày sinh", bg="light green").place(x=10, y=70)
 
    # tạo label "Email"
    email = Label(root, text="Email", bg="light green").place(x=10, y=90)
 
    # tạo label "Số điện thoại"
    sdt = Label(root, text="Số điện thoại", bg="light green").place(x=10, y=110)
 
    # Tạo label "Học kỳ"
    hocky = Label(root, text="Học kỳ", bg="light green").place(x=10, y=130)
 
    # Tạo label "năm học"
    namhoc = Label(root, text="Năm học", bg="light green").place(x=10, y=150)
    # tạo label "Chọn môn học"
    chonmonhoc = Label(root, text="Chọn môn học", bg="light green").place(x=10, y=170)



    # tạo ô mã số sinh viên và vị trí xuất hiện
    mssv_field = Entry(root, width=51)
    mssv_field.place(x=130, y=30)
    # tạo ô nhập họ tên và vị trí xuất hiện
    hoten_field = Entry(root, width=51)
    hoten_field.place(x=130, y=50)
    # tạo ô nhập ngày sinh và vị trí xuất hiện
    ngaysinh_field = Entry(root, width=51)
    ngaysinh_field.place(x=130, y=70)
    # tạo ô nhập email và vị trí xuất hiện
    email_field = Entry(root, width=51)
    email_field.place(x=130, y=90)
    # tạo ô nhập số điện thoại và vị trí xuất hiện
    sdt_field = Entry(root, width=51)
    sdt_field.place(x=130, y=110)
    # tạo ô nhập học kỳ và vị trí (.place) vị trí xuất hiện
    hocky_field = Entry(root, width=51)
    hocky_field.place(x=130, y=130)
    #tạo ô combobox để chọn năm học, điền dữ liệu thông qua ['value] = ('giá trị')
    namhoc_field = ttk.Combobox(root, width=48)
    namhoc_field.place(x=130, y=150)
    namhoc_field['values'] = (' 2022 - 2023', 
                      ' 2023 - 2024',
                      ' 2024 - 2025',
                      )
    # mặc định xuất hiện giá trị ở vị trí (0)
    namhoc_field.current(0)

    # tạo 4 checkbutton
    cbPython = Checkbutton(root, text="Lập trình Python", variable=var1,bg="light green").place(x=125, y =175)
    cbJava = Checkbutton(root, text="Lập trình Java", variable=var2,bg="light green").place(x=290, y =175)
    cbCnpm = Checkbutton(root, text="Công nghệ phần mềm", variable=var3,bg="light green").place(x=125, y =210)
    cbPTUDW = Checkbutton(root, text="Phát triển ứng dụng web", variable=var4,bg="light green").place(x=290, y =210)
    # tạo nút đăng ký và nút thoát, nút đăng ký lấy từ hàm submit
    btnDangKy = Button(root, text="Đăng ký", font=("arial", 11, "bold"), bd=1, fg="black", bg="dark green", command=submit).place(x=150, y=260)
    btnThoat =Button(root, text="Thoát",font=("arial",11, "bold"),bd=1, fg="black",bg="dark green",command=exit).place(x=330, y=260)
    # kiểm tra xem nhập đúng mã số sinh viên, email, số điện thoại, học kỳ, ngày sinh thông qua các hàm đã tạo trước đó
    mssv_field.bind("<FocusOut>", validate_mssv_input)
    email_field.bind("<FocusOut>", lambda e: validate_email_input())
    sdt_field.bind("<FocusOut>", validate_sdt_input)
    hocky_field.bind("<FocusOut>", validate_hocky_input)
    ngaysinh_field.bind("<FocusOut>", lambda e: validate_ngaysinh_input())
def create_child_window():
    child_window = Tk.Toplevel(root)
    child_window.title("Form Con")
    
    # Thêm các thành phần và widget vào form con
    label = ttk.Label(child_window, text="Đây là form con").place(x=380, y=290)
    # label.pack()
    
    button_close = ttk.Button(child_window, text="Đóng", command=child_window.destroy).place(x=380, y=290)
    button_close.pack()
    
    
root.mainloop()

    
 