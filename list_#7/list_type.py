'''
Topic #7: List trong Python - mạng dạng dữ liệu cho phép lưu trữ nhiều trong kiểu dữ liệu khác nhau trong nó \
và có thể truy xuất phần tử thông qua vị trí của phần tử trong list \

Ngôn ngữ khác như C/C++, Java, List trong Python tương đương với Mảng (Array)
''' 

'''
1. Create a list
'''
# list_1 = ["banana", "apple", "orange", "cherry"] # cùng kiểu string
# print(list_1)
# list_2 = [5, "house360.vn", False, 6.9] # list có thể chứa các phần tử khác kiểu
# print(list_2)
# list_3 = list() # khai báo list rỗng
# print(list_3)

'''
2. Access elements: truy cập đến các giá trị trong list
'''
# my_list = [1, 2, 3, 3, 3, '3','3', True]
# print(len(my_list)) # độ dài của list hay list có bao nhiêu phần tử
# print(my_list[2]) # truy cập giá trị của phần tử thứ 3 (index là 2, phần tử đầu tiên index là 0)

'''
tìm vị trí (index) của giá trị cần tìm, nếu có trả ra index đầu tiên tìm thấy
không thì trả lỗi "ValueError: '2' is not in list"
'''
# print(my_list.index('3'))

# count(): đếm phần tử xuất hiện bao nhiêu lần trong list
# print(my_list.count(3)) # 3
# print(my_list.count('3')) # 2
# print(my_list.count('6')) # 0

# duyệt list
# for item in my_list:
#     print(item)

'''
Python's built-in enumerate function allows us to loop over a list and retrieve both
the index and the value of each item in the list.
'''
# presidents = ["Washington", "Adams", "Jefferson", "Madison", 
#               "Monroe", "Bush", "Jackson"]
# print(presidents)
# for index, president in enumerate(presidents, start=1): # index bắt đầu từ 0, muốn bắt đầu từ 1 thì dùng start=1
#     print(f"President {index}: {president}")

'''
Slicing is called slicing and has the format [start: end: step]
'''
# my_list = [1, 2, '3', True]
# print(my_list[1:]) # từ index 1 đến hết list: [2, '3', True]
# print(my_list[:2]) # từ index 0 đến 1 (upto, not include): [1, 2]
# print(my_list[-1]) # lấy phần tử cuối của list, phânf tử -1: True
# print(my_list[::2]) # cắt list với step bằng 2: [1, '3']
# print(my_list[::-1]) # đảo ngược list: [True, '3', 2, 1]

'''
3. List operations & useful methods
    3.1 Add to List

'''
# my_list = [1, 2, '3', True]
# # không thay đổi list
# print(my_list*2) # tạo list mới bằng double list đã có: [1, 2, '3', True, 1, 2, '3', True]
# print(my_list + [100, "house360.vn"]) # tạo list mới bằng toán tử +: [1, 2, '3', True, 100, 'house360.vn']
# # thay đổi list
# my_list.append(100) # add thêm phần tử vào list
# print(my_list) # [1, 2, '3', True, 100]
# my_list.extend([200, 'house360.vn']) # thêm nhiều phần tử vào list
# print(my_list) # [1, 2, '3', True, 100, 200, 'house360.vn']
# my_list.insert(3,4) # thêm phần tử vào list tại vị trí bất kì
# print(my_list) # [1, 2, '3', 4, True, 100, 200, 'house360.vn']

'''
    3.2 Remove from list
'''
# my_list = [1, 2, '3', True]
# my_list.pop() # remove phần tử cuối cùng của list
# print(my_list) #  [1, 2, '3']
# my_list.pop(2) # remove index bất kì
# print(my_list) # [1, 2, True]

# my_list = [1, 2, '3', True, 2, 2]
# my_list.remove(2) #remove phần tử đầu tiên tìm thấy: [1, '3', True, 2, 2]
# print(my_list) # [1, '3', True, 2, 2]
# del my_list[2] # remove by index
# print(my_list) # [1, 2, True, 2, 2]

'''
    3.3 Sorting, note that elements have the same type
'''
# my_list = [1, 4, 2, 8, 3, 0]
# thay đổi list
# my_list.sort() # sort tăng dần
# print(my_list)
# my_list.sort(reverse=True) # sort giảm dần
# print(my_list) # [8, 4, 3, 2, 1, 0]
# my_list.reverse() # đảo list, không sắp xếp
# print(my_list) # [0, 3, 8, 2, 4, 1]

# không thay đổi list
# print(sorted(my_list)) # [0, 1, 2, 3, 4, 8]
# print(my_list) # [1, 4, 2, 8, 3, 0]
# print(list(reversed(my_list))) # [0, 3, 8, 2, 4, 1]
# print(my_list) # [1, 4, 2, 8, 3, 0]

'''
    3.4 Useful methods
'''
# my_list = [1, 4, 2, 8, 3, 0]
# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))


