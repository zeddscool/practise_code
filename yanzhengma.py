import random

def generate_code(code_length = 4):
    all_chars = '1234567890abcdefghijklmnopqrstuvwxyz'
    a = len(all_chars) - 1
    code = ''
    for i in range(code_length):
        index = random.randint(0, a)
        code += all_chars[index]
    return code
