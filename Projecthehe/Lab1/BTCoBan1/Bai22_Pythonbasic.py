#22. Write a Python program to count the number 4 in a given list.
def Dem(nums):
    dem=0 #gán giá trị đếm bằng 0
    for num in nums: # duyệt
        if num == 4: 
            dem = dem +1 # nếu gặp số 4 thì tăng lên 1
    return dem
print(Dem([1,2,3,4,5,4,4,4]))
print(Dem([1,2,3,4,5,4,4,4,4,4,4,4]))