# Пользователь два раза вводит слова через пробел (только буквы и пробел).
# Вывести только слова, которые есть в обеих вводах.

user_input1 = input("Your first input: ")
user_input2 = input("Your second input: ")

result_input = (user_input1+user_input2).replace(" ", "")
print(result_input)
