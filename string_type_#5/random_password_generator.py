'''
Project: Random Password Generator

Password: abcXYZ-69_96
'''

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

# print(LETTERS)
# print(NUMBERS)
# print(PUNCTUATION)

def password_generator(length=8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)

    return random_password

def check_digit_input(input_str):
    for chr in input_str:
        if chr not in NUMBERS:
            return False
    return True

def get_password_length():
    while True:
        password_length = input("Please input your password length: ")
        if check_digit_input(password_length):
            return int(password_length)
        else:
            continue
    return 8 # default

def main():
    password_length = get_password_length()
    password = password_generator(password_length)
    print(password)

if __name__ == "__main__":
    main()