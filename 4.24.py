print("Vo Van Dao")
print("MSSV:235752021610060")
print("###################")
###########################
def count_case(senence):
    uppercase_count = 0
    lowercase_count = 0
    for char in sentence:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
print(f"Số lượng chữ hoa: {'uppercase_count'}")
print(f"Số lượng chữ thường: {'lowercase_count'}")
sentence = input("Nhập một câu: ")
count_case(sentence)
