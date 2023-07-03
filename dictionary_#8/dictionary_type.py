'''
Topic 8 - Dictionary: một tập hợp key-value không có thứ tự, có thể thay đổi và lập chỉ mục
Dictionary được khởi tạo với các dấu ngoặc nhọn {} và chúng có các khoá và giá trị (key-value).
Mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất,
trong khi đó value có thể là bất kỳ kiểu giá trị nào.

Key phải là một kiểu không thể thay đổi (immutable) như chuỗi, sô hoặc tuple.
'''

# Create a new dictionary: a dictionary is a collection which is unordered, changeable and indexed.
# A dictionary consists of a collection of key-value pairs.

# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'} # tạo bằng dấu {}
# print(my_dict)
# my_dict2  = dict(name='house360.vn', conttent='Programming Youtube Channel', city='Ho Chi Minh') # tạo bằng hàm dict()
# print(my_dict2)

# Access item
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# content_in_dict = my_dict['content']
# print(content_in_dict)
# print(my_dict['age']) # KeyError: 'age'

# Check for key, use if .. in .. and try .. except
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# if 'name' in my_dict:
#     print(my_dict['name']) # house360.vn
# else:
#     print('No key found')
# if 'age' in my_dict:
#     print(my_dict['name']) # house360.vn
# else:
#     print('No key found') # No key found
# try:
#     print(my_dict['age'])
# except KeyError:
#     print("No Key Found") # No key found

# Add and change items (key-value) pairs
# # Add a new key
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# my_dict['email'] = 'admin@house360.vn'
# print(my_dict)
# # or overwrite the value on existing key
# my_dict['email'] = 'admin@house360.com.vn'
# print(my_dict)

# Delete items
# delete a key-value pair
# dùng keyword del
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# del my_dict['city']
# print(my_dict) # {'name': 'house360.vn', 'content': 'Programming Youtube Channel'}

# delete item dùng hàm pop()
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# print(my_dict.pop('city')) # xoá item dựa vào key và trả ra value: Ho Chi Minh
# print(my_dict) # {'name': 'house360.vn', 'content': 'Programming Youtube Channel'}

# delete item dùng hàm popitem(), từ python 3.7 hàm popitem remove item cuối cùng insert vào dictionary
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# my_dict['age'] = 25
# print(my_dict) # {'name': 'house360.vn', 'content': 'Programming Youtube Channel', 'city': 'Ho Chi Minh', 'age': 25}
# my_dict.popitem()
# print(my_dict) # {'name': 'house360.vn', 'content': 'Programming Youtube Channel', 'city': 'Ho Chi Minh'}

# Loop through Dictionary
# loop over keys
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# for key in my_dict:
#     print(key, my_dict[key])
# for key in my_dict.keys(): # giống như trên
#     print(key, my_dict[key])
# loop over values
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# for value in my_dict.values():
#     print(value)

# loop over keys and values
# my_dict = {'name':'house360.vn', 'content':'Programming Youtube Channel', 'city': 'Ho Chi Minh'}
# for key, value in my_dict.items():
#     print(key, value)
