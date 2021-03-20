"""
Домашнее задание №1
Функции и структуры данных
"""
import math


def power_numbers(*number):
    """
       функция, которая принимает N целых чисел,
       и возвращает список квадратов этих чисел
       """
    return [number ** 2 for number in number]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(args):
    """
    функция, которая принимает целое число,
        и проверяет является ли число простым
    """
    if args <= 1:
        return False
    if args <= 3:
        return True
    for i in range(2, args-1):
        if (args % i) == 0:
            return False
    return True


def filter_numbers(args, type):
    if type == "odd":
        return list(filter(lambda x: x % 2 == 1, args))
    if type == "even":
        return list(filter(lambda x: x % 2 == 0, args))
    if type == "prime":
        return list(filter(lambda x: is_prime(x), args))

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
