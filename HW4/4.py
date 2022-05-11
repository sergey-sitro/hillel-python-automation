# Пользователь вводит число. Используя list comprehension создать список кубов
# всех чисел от нуля до числа пользователя (не включая его), если текущее число минус 1
# (число текущей итерации для которого считается куб) кратно 3.

user_input = int(input("Enter a number: "))

cube_number = [i**3 for i in range(0, user_input) if (i - 1) % 3 == 0]
print(cube_number)
