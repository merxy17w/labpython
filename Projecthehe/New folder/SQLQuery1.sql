-- Tạo cơ sở dữ liệu
CREATE DATABASE QuanLyDanhBa12;

-- Sử dụng cơ sở dữ liệu mới tạo
USE QuanLyDanhBa12;

-- Tạo bảng Nhóm danh bạ
CREATE TABLE ContactGroups (
    ID INT PRIMARY KEY IDENTITY(1,1),
    TenNhom NVARCHAR(255) NOT NULL
);

-- Tạo bảng Liên hệ
CREATE TABLE Contacts (
    ID INT PRIMARY KEY IDENTITY(1,1),
    HoTen NVARCHAR(255) NOT NULL,
    DiaChiEmail NVARCHAR(255),
    SoDienThoai NVARCHAR(20),
    DiaChi NVARCHAR(255),
    NgaySinh DATE,
    IDNhom INT
    
);

-- Chèn dữ liệu mẫu vào bảng Nhóm danh bạ
DELETE FROM Contacts;
DBCC CHECKIDENT ('Contacts', RESEED, 1);
TRUNCATE TABLE Contacts;
-- Chèn dữ liệu mẫu vào bảng Liên hệ
INSERT INTO Contacts (HoTen, DiaChiEmail, SoDienThoai, DiaChi, NgaySinh, IDNhom)
VALUES
    (N'Phạm Anh Quân', 'lucy17w@email.com', '0842728528', '159 hehe', '2003-10-17', 1),
    (N'Trần Văn Nam', 'thichbulu@email.com', '0559368123', '93 Võ Trường Toản', '2003-05-06', 2),
    (N'Xuân Quang lonton', 'xq111@email.com', '0879089892', '87 ngo quyen','2003-11-01', 3),
	(N'Đinh Lê Quang Huy', 'ricon@email.com', '0559368452', '29 Phù Đổng', '2003-06-30', 2),
	(N'Lê Tấn Đan Huy', 'yuongboisitinh@email.com', '0399363532', '293 Trần Khánh Dư', '2003-06-10', 2),
	(N'Nguyễn Ngọc Tú', 'thichbukhu@email.com', '0849283942', '293 tran quoc toan', '2003-03-12', 2),
	(N'Lê Ngọc Hoàng Chương', 'lonkhongcoco@email.com', '0849274617', '293 tran quoc toan', '2003-04-03', 2),
	(N'Tu Thị Hồng Thương', 'thuong@email.com', '0824928472', '293 Nguyễn Văn Linh', '2003-04-07', 2);