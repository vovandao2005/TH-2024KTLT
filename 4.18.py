print("Vo Van Dao")
print("MSSV:235752021610060")
print("###################")
###########################
n = int(input("Nhập số nguyên n: "))
fibonacci_list = []
a, b = 0, 1

while a < n:
    fibonacci_list.append(a)
    a, b = b, a + b
print("Các số Fibonacci nhỏ hơn", n, "là:", fibonacci_list)
