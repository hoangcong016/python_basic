'''
    4. List Comprehensions
'''
'''
List Comprehension giúp cho bạn viết code ngắn gọn (đặc biệt khi đang ở trong một vòng lặp đã có)
và dễ đọc, nhìn code hơn.
'''
# new_list[<action> for <item> in <interator> if <some condition>]

# word = "Hello World"
# list_word = [char for char in word] # list_word = list(word)
# print(list_word)

# even_numbers = [i for i in range(0, 10) if i%2 == 0] # tạo list số chẵn trong phạm vi
# print(even_numbers)

# Ví dụ: tính giá hoá hơn khi thêm thuế và phí dịch vụ
# transactions = [100, 200, 300, 150, 80]
# TAX_RATE = 0.08
# SERVICE_CHARGE = 0.07
# def get_price_tax_service(bill):
#     return bill*(1 + TAX_RATE + SERVICE_CHARGE)
# # print(get_price_tax_service(100)) # test
# final_prices = [get_price_tax_service(bill) for bill in transactions]
# print(final_prices)

'''
Advanced Functions
'''
# list() to convert string to list
# my_string = "Hello, welcome to house360.vn!"
# list_of_chars = list(my_string)
# print(list_of_chars)

# sum()
# print(sum([1,5,2,9,4]))

# zip(): looping through two list simultaneously
# wizards = ["Harry Potter", "Ron", "Hermione"]
# pets = ["Hedwig", "Scabber", "Crookshank"]
# for wiz, pet in zip(wizards, pets):
#     print(f"{wiz} has {pet}")
# # 0 ['Harry Potter', 'Hedwig']
# # 1 ['Ron', 'Scabber']
# # 2 ['Hermione', 'Crookshank']
# for index, (wiz, pet) in enumerate(zip(wizards, pets)):
#     print(f"{index + 1}. {wiz} has {pet}")

# sorted()
# my_str_list = ["Hello", "welcome", "to", "house360.vn"]
# sorted_by_first = sorted(my_str_list)
# print(sorted_by_first) # ['Hello', 'house360.vn', 'to', 'welcome']
# sorted_by_second = sorted(my_str_list, key=lambda el: el[1])
# print(sorted_by_second) # ['Hello', 'welcome', 'to', 'house360.vn']

# list_dic = [{'name': 'House360.vn', 'age': 0 }, {'name': 'Peter', 'age': 5}, {'name': 'Mary', 'age': 18}]
# sorted_by_key = sorted(list_dic, key=lambda el: el['name']) 
# print(sorted_by_key) # [{'name': 'House360.vn', 'age': 0}, {'name': 'Mary', 'age': 18}, {'name': 'Peter', 'age': 5}]
# sorted_by_value = sorted(list_dic, key=lambda el: el['age']) 
# print(sorted_by_value) # [{'name': 'House360.vn', 'age': 0}, {'name': 'Peter', 'age': 5}, {'name': 'Mary', 'age': 18}]

'''
    5. 2D Array/List = Matrix: Mảng 2 chiều
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# print(matrix[1][2]) # 6
# print(matrix[2][1]) # 8
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         print(matrix[row][col])

# Transform Matrix to List
# list_converted = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
# print(list_converted) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Combine columns with zip and *
matrix_columns = [x for x in zip(*matrix)]
print(matrix_columns) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]