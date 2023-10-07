
day_list = ["Thứ 2","Thứ 3","Thứ 4" ,"Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
while True:
    num =int(input("Nhập số từ 1 đến 6: "))
    if num >=0 and num <= 6:
        print("Hôm nay là "+ day_list[num])
        break
    else:
        print("Nhập lại!")
