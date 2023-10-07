#Viết chương trình cho người dùng nhập 1 số từ 0..6, nếu người dùng nhập 0 thì xuất ra màn hình “Hôm nay là chủ nhật”, người dùng nhập 1 thì xuất hôm nay là thứ 2, …, người dùng nhập 6 thì xuất “Hôm nay là thứ bảy”; 

def KiemTra(num:int):
    match num:
        case 0:
            return "thứ 2"
        case 1:
            return "thứ 3"
        case 2:
            return "thứ 4"
        case 3:
            return "thứ 5"
        case 4:
            return "thứ 6"
        case 5:
            return "thứ 7"
        

while True:
    num = int(input("Nhập số:"))  
    ThongBao = KiemTra(num)
    if(num > 0 and num <= 6):
        print(f"Hôm nay là {ThongBao}")
        break
    else:
        print ("Số sai!") 
'''if num< 0:
    print ("Số sai!" )  
elif num > 6:
          
else:
    print(f"Hôm nay là {ThongBao}")'''
    