# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def random_str(min_range: int = 1, max_range: int = 15) -> str:
    random_range = range(random.randrange(min_range, max_range))
    random_string = ''.join((random.choice(string.ascii_lowercase) for _ in random_range))

    return random_string


def generate_random_name():
    while True:
        yield f'{random_str()} {random_str()}'


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
