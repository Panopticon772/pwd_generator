import random

symbols = [
    '!',
    '@',
    '#',
    '$',
    '%',
    '&',
    '*'
]

numbers = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
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


def random_letter():
    case = random.randint(0, 1)
    if case == 0:
        return random.choice(letters).capitalize()
    else:
        return random.choice(letters)


def random_symbol():
    return random.choice(symbols)


def random_number():
    return random.choice(numbers)


def generate_pwd(pwd_length):
    pwd_arr = []
    i = 0
    while i < pwd_length:
        random_character = random.randint(0, 2)
        # if 0, returns random letter
        if random_character == 0:
            print('randomn letter:', random_letter())
            pwd_arr.append(random_letter())
        # if 1, returns random symbol
        elif random_character == 1:
            print('randomn symbol:', random_symbol())
            pwd_arr.append(random_symbol())
        # if 2, returns random number
        else:
            print('randomn number:', random_number())
            pwd_arr.append(random_number())
        i += 1
    pwd = ''.join(map(str, pwd_arr))
    print(f'Your new password is: {pwd}')


create_pwd = True

while create_pwd == True:
    pwd_length = int(input(
        'Please enter the length of the password you desire. Must be a number between 8 and 16. '
    ))
    if pwd_length >= 8 and pwd_length <= 16:
        generate_pwd(pwd_length)
        create_pwd = False
    else:
        print('Error: Password length does not meet requirements.')
