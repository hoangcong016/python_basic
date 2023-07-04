# my_list = [1, 2 , 3]
# for num in my_list:
#     print(num)

# my_dict = {'a':1, 'b': 2, 'c':3}
# for key,value in my_dict.items():
#     print(key, value)

'''
while <condition that evaluates to boolean>:
    # action
    if <condition that evaluates to boolean>:
        break # break out of while loop
    if <condition that evaluates to boolean>:
        continue # continue to the next line in the block
'''
msg = ''
while msg != 'quit':  # nếu msg được nhập khác quit thì tiếp tục lập
    msg = input('Please give me an input: ')
    print(msg)