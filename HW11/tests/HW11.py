def is_even(number):
    """
    Принимает один аргумент
    Возвращает True - если он четный
    Возвращает False - если не четный
    """
    return number % 2 == 0


def is_odd(number):
    """
    Принимает один аргумент
    Использует функцию is_even из глобальной области видимости
    Внути нельзя использовать if/else
    Возвращает False - если он четный
    Возвращает True - если не четный
    """
    return not is_even(number)


def custom_max(num1, num2):
    """
    Принимает два аргумента
    Не использовать фнукцию max внути
    Возвращает наибольший из двух элементов
    """
    return num1 if num1 > num2 else num2


def multiply(*args, base=1):
    """
    Принимает любое кол-во аргументов и один дополнительный необязательный именованный аргумент base
    base по умолчанию равен 1
    Возвращает результат перемножения всех переданных аргументов и необязательного
    """
    result = 1
    for i in args:
        result *= i
    return result * base


example_list = list(range(1, 10))


def reverse(string):
    """
    Принимает один аргумент, строку
    Возвращает развернутую строку
    """
    return string[::-1]


def upper_count(string):
    """
    Принимает один агрумент, строку
    Возвращает кол-во букв в верхнем регистре
    """
    return len([letter for letter in string if letter.isupper()])


def unique(lst):
    """
    Принмает один аргумент, список
    Возвращает список уникальных элементов этого списка отсортированных от меньшего к большему
    """
    return sorted(list(set(lst)))


def is_pangram(string):
    """
    Функция принимает один аргумент, строку
    Возвращает True если в строке хотя бы раз встречается каждая буква английского алфавита
    иначе возвращает False
    """
    alphabet = "abcdefghigjklmnopqrstuvwxyz"
    return all([a in string.replace(" ", "").lower() for a in alphabet])
