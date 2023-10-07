'''25. Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''
def KiemTra(chuoi, num):
    for giatri in chuoi:
        if num == giatri:
            return True
    return False
print(KiemTra([1,2,3,4,5,6],3))
print(KiemTra([1,2,3,4,5,6],7))