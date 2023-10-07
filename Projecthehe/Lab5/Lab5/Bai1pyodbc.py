import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};Server=WINDOWS-10\SQLEXPRESS;DATABASE=QuanLyDanhBa12;')

cursor = conn.cursor()
cursor.execute("SELECT @@version")
db_version = cursor.fetchone()
cursor.close()  # Đóng con trỏ sau khi hoàn tất công việc
conn.close()  # Đóng kết nối

print("Bạn đang dùng hệ quản trị CSDL SQL Server phiên bản", db_version)