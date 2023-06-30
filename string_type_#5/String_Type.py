'''
Topic #2: Strings (Chuỗi Ký Tự) - a sequence of characters
'''

# String: ordered, immutable,  text presentation

# use single or double quotes
# my_string = '' # Chuỗi rỗng
# print(type(my_string))
# my_string = 'Hello, World!' # single quotes
# print(my_string)
# my_string = "Hello, World!" # double quotes
# print(my_string)
# my_string = '''Hello, World!''' # triple quotes from python 3.6
# print(my_string)

# usecases
# my_string = "My name 's house360.vn" # have single quote in text
# print(my_string)
# my_string = 'Some one said that: "life is short, ..."' # have double quotes in text
# print(my_string)
# my_string = '''I'm a "Single Dad"''' # have single and double quotes in text
# print(my_string)
# my_string = 'I\'m a "Single Dad"' # have single and double quotes in text, use Escaping backslash
# print(my_string)
# my_string = "I'm a \"Single Dad\"" # have single and double quotes in text, use Escaping backslash
# print(my_string)

# backslash also uses to continue in next line
# my_string = "I'm from house360.vn, is a dev I want to learn new tech and \
# share my knowledge to the communication."
# print(my_string)

'''
Access characters and substrings
'''
my_string = "Hello, World!"
# get character by referring to index
# char0 = my_string[0]
# print(char0)
# print(my_string[-1]) # last character
# print(my_string[-2]) # next to last character

# String is immutable -> Cannot be changed
# my_string[0] = "M" # this line shows error: "TypeError: 'str' object does not support item assignment"

# Substrings with slicing
# string_name[startIndex:endIndex]
# sub_str1 = my_string[0:5] # start at index 0 and go until index 5 (not include index 5): "Hello"
# print(sub_str1)
# sub_str2 = my_string[1:5] # start at index 1 and go until index 5 (not include index 5): "ello"
# print(sub_str2)
# sub_str_from_start = my_string[:5] # start at index 0 and go until index 5 (not include index 5): "Hello"
# print(sub_str_from_start)
# sub_str_to_end = my_string[7:] # start at index 6 and go to end index: "Wolrd!"
# print(sub_str_to_end)

# revert_str = my_string[::-1] # Reverse the String: "!dlroW ,olleH"
# print(revert_str)
# take_str_by_step = my_string[::2] # Take every second character: "Hlo ol!"
# print(take_str_by_step)

'''
Concatenate two or more strings
'''
# concat strings with + (plus)
# channel_str = "house360.vn"
# greeting_str = "Hello, welcome to"
# sentence = greeting_str + " " + channel_str + "!"
# print(sentence)

# join elements of a list into a string: .join()
# my_list = ["How", 'are', 'you', 'doing', '?']
# sentence = ' '.join(my_list) # connect list by using a space
# print(sentence)

'''
Interating
'''
# Interating over a string by using a for in loop
my_str = "Welcome to Vietnam"

# for char in my_str:
#     print(char)

# if "V" in my_str: # check a char exists in string
#     print("Yes")
# else:
#     print("No")

'''
Basic & useful functions (Các hàm cơ bản và hữu ích)
'''

#strip() : remove specify character at the begin and end of a string
# print(" I'm from Vietnam   ".strip()) # trip() default will remove whitespace at the start and end of a string: "I'm from Vietnam"
# print(" I'm from Vietnam   I".strip("I")) # trip("<string>") will remove string at the start and end if match: " I'm from Vietnam   "

# split()
# print("Life is a present".split()) # split() default will splip string by whitespace: ['Life', 'is', 'a', 'present']
# print("but,  a lot of challenges".split(",")) # split by ",": ['but', '  a lot of challenges']

# replace
# print("Help me".replace("me", "you"))

# check, find functions
my_str = "Practice makes perfect"
# print(my_str.startswith("Practice")) #True
# print(my_str.endswith("Practice")) #False

# print(my_str.index("c")) # return first place found
# print(my_str.index("C")) # if not found, return ValueError: substring not found

# print(my_str.find('c')) # return first place found
# print(my_str.find('C')) # if not found, return -1

# change string
# my_str = "HOUSE 360 VN"
# print(my_str.lower()) # house 360 vn
# my_str = "house 360 vn"
# print(my_str.upper()) # HOUSE 360 VN
# print(my_str.title()) # House 360 Vn
# my_str = "ok, I'm fine, thank you!"
# print(my_str.capitalize()) # "Ok, i'm fine, thank you!", note that I'm turn to i'm => find solution for this

# count function
# my_str = "ok, I'm fine, thank you!"
# print(my_str.count("k")) # 2

'''
String Formatting
'''
# %, .format(), f-Strings

# %
# name = "HOUSE 360 VN"
# my_str = "My name is %s" % name # viết liền hay cách python đều hiểu
# print(my_str)

# pi = 3.14159
# s = "pi number"
# my_str = "Variable is %f from %s" %(pi, s) # hai tham số đầu vào trong chuỗi
# print(my_str)
# my_str = "Variable is %.2f from %s" %(pi, s) # hai tham số đầu vào trong chuỗi, float lấy 2 chữ số thập phân
# print(my_str)

# .format()
# age = 24
# height = 175.5
# name = "HOUSE 360 VN"
# my_str = "I am {}; {} years old; height {:.3f} cm".format(name, age, height)
# print(my_str)

# f-String (Python 3)
# age = 1
# height = 168.5
# name = "HOUSE 360 VN"
# my_str = f"I'm {name}, height {height:.3f} cm, {age} year old."
# print(my_str)