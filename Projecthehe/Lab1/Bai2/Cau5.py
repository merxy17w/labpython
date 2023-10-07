def Fibo(n:int): # dùng đẹe quy
    return 1 if n == 1 or n == 2 else Fibo(n-1) + Fibo(n-2)

def fibonacci(n):# không dùng đệ quy
    f0 = 0
    f1 = 1
    fn = 1
 
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
n = int(input("Nhập n: "))
check = Fibo(n)
kodequy = fibonacci(n)
print(kodequy)
print(check)