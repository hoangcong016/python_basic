# Basic Data Types
'''
Các kiểu dữ liệu cơ bản trong Python: bool, None, int, float, str
'''

'''
Topic #0: bool & NONE
'''

# [X] bool: True & False
var_bool = True

# [X] type(): Dynamically typed (không cần khai báo kiểu dữ liệu khi khai báo biến), C++ là Static Typed
#print(type(var_bool))

# Numberically, they're evaluated as integers with values: 1 (True), 0 (False)

a =  4 + True
#print(a)

b = False
# if  b == 0:
#     print("B is 0")

# [X] None: Phần Tử Không
var_none = None
#print(var_none)

# None is often used as a placeholder for optional or mising value.
# It evaluates as False in conditions.

#email_address = None #False
# email_address = 'admin@house360.vn'

# if email_address:
#     print(f"Email address is {email_address}")
# else:
#     print(f"Email address is empty or {email_address}")

'''
Topic #1: Number (int & float)
'''
# [X] Numbers: int (Integer = Số Nguyên) & float (Floating point numbers = Số Thực)
# print(type(1)) # int
# print(type(0))
# print(type(-10))

# print(type(0.0)) # float
# print(type(2.3))
# print(type(4E2), 4E2) # 4*10^2 là số thực

# [X] Arithmetic (Các phép toán): +, -, *, /, ** (hàm mũ), // (chia lấy nguyên), % (chia lấy dư)
# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10**3) # 10^3 = 10*10*10 = 1000
# print(10//3) # chia lấy ngyên: 10 chia 3 được 3 dư 1, vậy kết quả là 3
# print(10%3) # chia lấy dư: 10 chia 3 được 3 dư 1, vậy kết quả là 1

# Basic Functions (Các Hàm Cơ Bản)
print(pow(10,3))#10**3
print(abs(-6.9)) # trị tuyệt đối: 6.9
print(round(6.69)) #7
print(round(6.49)) #6
print(round(5.468, 2)) #5.47 -->round to nth digit
print(round(5.468, 5)) #5.46800, tìm hiểu print nhiều số 0 theo sau float
print(bin(512)) # hệ nhị phân (binary format)
print(hex(512)) # hệ thâp lục phân (hexadecimal format)

