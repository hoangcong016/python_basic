'''
Leetcode Palindrome: cho một chuỗi, đọc xuôi hay ngược đều giống nhau là Palindrome
Condition: bỏ qua viết hoa viết thường, các dấu như :, ', !
'''
def check_palindrome(str=""):
    if str == "":
        return True
    result = [] # list()
    for c in str.lower():
        if c.isalnum():
            result.append(c)
    return result == result[::-1]

def main():
    str_check = input("Please input your text: ")
    print(check_palindrome(str_check))

if __name__ == "__main__":
    main()