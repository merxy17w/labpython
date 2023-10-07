from datetime import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo=maSo
        self._hoTen=hoTen
        self._ngaySinh=ngaySinh
    
    @property
    def maSo(self):
        return self._maSo
    
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self._maSo=maso
    
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso))==7
    
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong=tenmoi
    
    def __str__(self) -> str:
        return [f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"]

    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMSSV(self, mssv: int):
        return [sv for sv in self.dssv if sv == mssv]
    
    def timVTSvTheoMSSV(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
            return -1
        
    def xoaSvTheoMSSV(self, maSo: int)->bool:
        vt = self.timSvTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten:str):
        return [sv for sv in self.dssv if (sv.hoTen.split(" ")[-1].upper()== ten.upper())]

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]
    
    def sortByName(self, type: str):
        if(type == "tang"):
            for i in range(len(self.dssv) - 1):
                for j in range(i+1, len(self.dssv)):
                    if(self.dssv[i].hoTen.split(" ")[-1].upper() > self.dssv[j].hoTen.split(" ")[-1].upper()):
                        self.dssv[i], self.dssv[j] = self.dssv[j], self.dssv[i]
        return self.xuat()

file = open('D:\python\Projecthehe\Lab 2\dssv.txt', "r", encoding="utf8")
read = file.readlines()
listSV = []
sv = []
for i in read:
    if i not in listSV:
        listSV.append(i.strip())

listSV.sort()
print(listSV)