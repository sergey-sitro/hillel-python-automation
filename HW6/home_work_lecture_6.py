def is_even(number):
    """
    Принимает один аргумент
    Возвращает True - если он четный
    Возвращает False - если не четный
    """
    return number % 2 == 0


assert is_even(1) is False
assert is_even(10) is True


def is_odd(number):
    """
    Принимает один аргумент
    Использует функцию is_even из глобальной области видимости
    Внути нельзя использовать if/else
    Возвращает False - если он четный
    Возвращает True - если не четный
    """
    return not is_even(number)


assert is_odd(2) is False
assert is_odd(11) is True


def custom_max(num1, num2):
    """
    Принимает два аргумента
    Не использовать фнукцию max внути
    Возвращает наибольший из двух элементов
    """
    return num1 if num1 > num2 else num2


assert custom_max(1, 10) == max(1, 10)
assert custom_max(100, 10) == max(100, 10)


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

assert multiply(*example_list) == 362880
assert multiply(*example_list, base=2) == 725760


def reverse(string):
    """
    Принимает один аргумент, строку
    Возвращает развернутую строку
    """
    return string[::-1]


assert reverse("") == ""
assert reverse("QWERqwer123!@#") == "#@!321rewqREWQ"


def upper_count(string):
    """
    Принимает один агрумент, строку
    Возвращает кол-во букв в верхнем регистре
    """
    return len([letter for letter in string if letter.isupper()])


assert upper_count("") == 0
assert upper_count("QWER qwer 123 !@#") == 4


def unique(lst):
    """
    Принмает один аргумент, список
    Возвращает список уникальных элементов этого списка отсортированных от меньшего к большему
    """
    return sorted(list(set(lst)))


assert unique([2, 2, 1, 5, 5, 2, 7]) == [1, 2, 5, 7]


def is_pangram(string):
    """
    Функция принимает один аргумент, строку
    Возвращает True если в строке хотя бы раз встречается каждая буква английского алфавита
    иначе возвращает False
    """
    alphabet = "abcdefghigjklmnopqrstuvwxyz"
    return all([a in string.replace(" ", "").lower() for a in alphabet])


assert is_pangram("The five boxing wizards jump quickly") is True
assert is_pangram("hello") is False
