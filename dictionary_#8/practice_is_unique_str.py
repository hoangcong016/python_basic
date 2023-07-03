# Practice: Is Unique - Implement an Algorithm to determine if a string has all unique characters
# example:
# str = "abcd" # Unique
# str1 = "aabcdee" # Not Unique

import unittest # để viết các hàm test cho functions

def check_is_unique_str(str=''):
    # Hint: Hash Table => Dict: key-value, 
    # if dict chưa có key thì add key, nếu dict đã có key rồi thì return False,
    # ngược lại hết chuỗi mà chưa return False thì return True
    char_dict = {} # tạo một dictionary rỗng
    for char in str: # duyệt chuỗi theo từng ký tự
        if char in char_dict:
            return False
        else:
            char_dict[char] = True
    return True

def main():
    input_str = input("Please input a text: ")
    print(check_is_unique_str(input_str))

class Test(unittest.TestCase):
    dataTrue = ['abcd', 'fgd 34r', ',', '']
    dataFalse = ['232abcd', 'ad gfh2 da', 'ô gô']

    def test_unique(self):
        # true check
        for test_case in self.dataTrue:
            actualResult = check_is_unique_str(test_case)
            self.assertTrue(actualResult)
        # false check
        for test_case in self.dataFalse:
            actualResult = check_is_unique_str(test_case)
            self.assertFalse(actualResult)


if __name__ == "__main__":
    # unittest.main() # run test case, phải đưa ra test case đúng, chuẩn xác
    main() # run app