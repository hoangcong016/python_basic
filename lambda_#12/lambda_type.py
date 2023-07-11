'''
Hàm Ẩn Danh - Lambda trong python
'''
# Lambda function is a small (one line) anonymous function
# that is defined without a name

# Example: a lambda function that adds 69 to the input argument

# lambda_test_func = lambda so: so + 69 # 1 dòng
# print(lambda_test_func(1))
# # hàm tương đương
# def lambda_test_func1(so): # hàm này mất 2 dòng
#     return so + 69
# print(lambda_test_func1(1))

# hàm lambda nhiều tham số
# lambda_test_func = lambda x,y,z: x+y+z
# print(lambda_test_func(1,3,4))

# Custom sorting using a lambda function as key parameter
# coordinate2D = [(6,9), (9,6), (-1,3), (2,10)]
# print(sorted(coordinate2D)) # [(-1, 3), (2, 10), (6, 9), (9, 6)]
# print(sorted(coordinate2D, key = lambda point: point[1])) # [(-1, 3), (9, 6), (6, 9), (2, 10)]

# Sort by condition
# number_list = [5, 3, -2, 4, 1, -1, -3, 4, 5]
# print(sorted(number_list)) # [-3, -2, -1, 1, 3, 4, 4, 5, 5]
# print(sorted(number_list, key = lambda x: abs(x))) # [1, -1, -2, 3, -3, 4, 4, 5, 5]

# map(func, seq): transforms each element with the function
# list_keyword = ['house360.vn', "welcome", "all of you"]
# print(list(map(lambda x : x.title(), list_keyword))) # ['House360.Vn', 'Welcome', 'All Of You']
# # Tương tự, dùng list comprehension
# new_list = [keyword.title() for keyword in list_keyword]
# print(new_list)

# filter(func, seq): return all elements for which func evaluates to True
# list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x%2!=0, list_number)))
# # Hàm tương đương (dùng list comprehension)
# new_list = [x for x in list_number if x%2!=0]
# print(new_list)

# dùng lambda cho hàm reduce
# reduce(func, seq): repeatedly applies the func to the elements and returns a single value.
# reduce func takes two arguments
from functools import reduce
sequence = [1, 3, 5, 6, 9, 2, 8]
print(reduce(lambda a, b: a+b, sequence)) # sum sequence: 34
print(reduce(lambda a,b: a if a>b else b, sequence)) # find max value: 9