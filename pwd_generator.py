import random

units = [
    '!',
    '@',
    '#',
    '$',
    '%',
    '&',
    '*',
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    'a',
    'b',
    'c',
    'd',
    'e',
    'f'
    'g',
    'h',
    'i',
    'j',
    'k',
    'l'
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]


def generate_pwd(pwd_length):
    pwd_arr = []
    i = 0
    while i < pwd_length:
        pwd_arr.append(random.choice(units))
        i += 1
    pwd = ''.join(map(str, pwd_arr))
    print(f'Your new password is: {pwd}')


create_pwd = True

while create_pwd == True:
    pwd_length = int(input(
        'Please enter the length of the password you desire. Must be a number between 8 and 12. '
    ))
    if pwd_length >= 8 and pwd_length <= 12:
        generate_pwd(pwd_length)
        create_pwd = False
    else:
        print('Error: Password length does not meet requirements.')
