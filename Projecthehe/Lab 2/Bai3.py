class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self):
        return "{}/{}".format(self.tu, self.mau)
    def __eq__(self, other):
        return self.tu == other.tu and self.mau == other.mau

    @staticmethod
    def __TimUCLN(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def RutGon(self):
        ucln = self.__TimUCLN(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq
    
    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.RutGon()
        return kq

a = PhanSo(7, 3)
b = PhanSo(2, 3)
print(f"Phan so a: {a}")
print(f"Phan so a: {b}")
print(f"a + b = {a} + {b} = {a + b}")
print(f"a - b = {a} - {b} = {a - b}") 
print(f"a * b = {a} * {b} = {a * b}")
print(f"a * b = {a} / {b} = {a / b}")