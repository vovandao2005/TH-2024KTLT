print("Vo Van Dao")
print("MSSV:235752021610060")
print("######################")
################################
S = input("Nhập chuỗi: ")
for char in S:
    if char not in (' ', '\t'):
        print(char.upper())
