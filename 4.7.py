print("Vo Van Đạo")
print("MSSV:23575201610060")
print("###################")
###########################
input_string = input("Nhập chuỗi: ")
result_string = ''.join([char for char in input_string if not char.isdigit()])
print("Chuỗi sau khi loại bỏ chữ số:", result_string)
