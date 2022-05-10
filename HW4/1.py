# Пользователь вводит одно число - любое значение которое гарантированное можно перевести в int.
# Определить его кратность 2, 3, 5, 7 или самому себе.
# Вывести строку f"multiple of {val}" где val - значение кратности.
# Если число кратно нескольким значениям - выводить только наименьшее.
# Не используйте циклы в этой задаче. Используйте конструкцию if/elif/.../elif/else для того
# что бы проверить каждый из вариантов кратности.

user_input = int(input("Enter a number: "))

val = 0

if user_input % 2 == 0:
    val = 2
elif user_input % 3 == 0:
    val = 3
elif user_input % 5 == 0:
    val = 5
elif user_input % 7 == 0:
    val = 7
elif user_input % user_input == 0:
    val = user_input

print(f"multiple of {val}")
