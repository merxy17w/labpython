# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def XuLy(x,y,z):
    sum = x + y + z 
  
    if x == y == z: # nếu 3 số bằng nhau, nhân
      sum = sum * 3
    return sum
print(XuLy(1, 2, 3))
print(XuLy(3, 3, 3))

