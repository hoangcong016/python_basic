# Lesson #11

# Hàm với tham số
# def print_name(name): # name ở đây được gọi là parameter (tham số)
#     print(name)

# def main():
#     name = 'house360.vn'
#     print_name(name) # name ở đây được gọi là argument (biến)

# Tham số bắt buộc (required parameter), hàm bắt buộc phải truyền đủ tham số
# def print_name(name, greeting):
#     print(f'{name}, {greeting}')

# def main():
#     name = 'house360.vn'
#     greeting = 'Welcome to '
#     # print_name(name) # TypeError: print_name() missing 1 required positional argument: 'greeting'
#     print_name(name, greeting) # house360.vn, Welcome to

# if __name__ == "__main__":
#     main()

# # Tham số mặc định (default parameter): tham số default nếu không được truyền khi gọi hàm sẽ lấy giá trị mặc định
# def print_name(name, greeting='Welcome to '): # greeting has default value is: "Welcome to "
#     print(f'{name}, {greeting}')

# def main():
#     name = 'house360.vn'
#     greeting = 'Bye Bye!'
#     print_name(name) # lấy giá trị mặc định của tham số greeting: "house360.vn, Welcome to "
#     print_name(name, greeting) # ghi đè lên giá trị mặc định của biến greeting: "house360.vn, Bye Bye!"

# if __name__ == "__main__":
#     main()

# # Position & Keyword Arguments
# def print_name(name, age, greeting='Welcome to '):
#     print(f'{name}, {age}, {greeting}')

# def main():
#     nameValue = 'house360.vn'
#     ageValue = 0
#     greetingValue = 'Bye Bye!'
#     print_name(nameValue, ageValue, greetingValue) # positional arguments: house360.vn, 0, Bye Bye!
#     print_name(name=nameValue, greeting=greetingValue, age=ageValue) # keyword arguments: house360.vn, 0, Bye Bye!
#     print_name(name=nameValue, age=ageValue) # keyword arguments and default parameter: house360.vn, 0, Welcome to

# if __name__ == "__main__":
#     main()

# Variable-length parameters (*args and **kwargs)
# If you mark a parameter with one asterisk (*)
# you can pass any number of positional arguments to your function (Typically called *args)
# def variableLengthArgsExample(a, b, *args):
#     print(f'{a}, {b}')
#     for arg in args: # args is as a list
#         print(arg)

# def main():
#     variableLengthArgsExample('a', 'b', "Hello *agrs", 1, 2, 3, 5, 8)

# if __name__ == "__main__":
#     main()

# If you mark a parameter with two asterisk (**)
# you can pass any number of keyword arguments to your function (Typically called **kwargs)
# def variableLengthArgsExample(a, b, **kwargs):
#     print(f'{a}, {b}')
#     for key, value in kwargs.items(): # kwargs is as a dictionary
#         print(key, value)

# def main():
#     variableLengthArgsExample('a', 'b', size='XXL', age='NG')

# if __name__ == "__main__":
#     main()

# Kết hợp cả *args and **inikwargs, trong khi hàm được gọi, có truyền giá trị cho tham số *args hay **kwargs
# hay không cũng không báo lỗi, có thì dùng không có thì thôi
def variableLengthArgsExample(a, b, *args, **initkwargs):
    print(f'{a}, {b}')

    for arg in args:
        print(arg)

    for key, value in initkwargs.items():
        print(key, value)

def main():
    variableLengthArgsExample('a', 'b', 1, 2, 3, size='XXL', age='NG') # có cả *args và **kwargs
    variableLengthArgsExample('a', 'b', size='XXL', age='NG') # không có *args, chỉ có **kwargs
    variableLengthArgsExample('a', 'b', 1, 2, 3) # có *args, không có **kwargs
    variableLengthArgsExample('a', 'b') # không có *args lẫn **kwargs

if __name__ == "__main__":
    main()