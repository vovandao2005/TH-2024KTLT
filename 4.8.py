print("Vo Van Dao")
print("MSSV:235752021610060")
print("#####################")
##########################
input_string = input("Nhập dãy các từ: ")
words = input_string.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất có độ dài", max_length, "là:", ", ".join(longest_words))
