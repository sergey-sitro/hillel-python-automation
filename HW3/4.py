# Есть список (в 1-й строке вашего скрипта созданный вами, я его могу заменить
# на любой другой во время проверки) из случайного кол-ва элементов (минимум 10).
# Пользователь вводит начало, конец и шаг слайса - вывести слайс

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user_input_start = int(input("Start of slice: "))
user_input_end = int(input("End of slice: "))
user_input_step = int(input("Step of slice: "))

print(list1[user_input_start:user_input_end:user_input_step])
