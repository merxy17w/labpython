#20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def ChuoiMoi(text, n):
   kq = "" 
   for i in range(n):
      kq = kq + text
   return kq
print(ChuoiMoi('abc', 2))
print(ChuoiMoi('.py', 3)) 
