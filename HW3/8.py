# 0) Инициализировать пустой словарь
# 1) Спросить имя пользователя и добавить его в словарь
# 2) Спросить возраст пользователя и добавить его в словарь
# 3) Спросить названия любимых фильмов пользователя, введенных через запятую, и добавить их в словарь списком
# 4) Вывести пользователю весь словарь
# 5) Вывести пользователю список ключей словаря
# 6) Спросить пользователя какой элемент заменить
# 7) Спросить пользователя на какую строку заменить элемент
# 8) Заменить указанный элемент на указанную строку
# 9) Вывести словарь
# 10) Попросить пользователя ввести ключ который может быть а может не быть в словаре
# 11) Запросить значение которое вывести если в словаре нет этого ключа
# 12) Вывести значение из словаря или пользовательское

user_dict = {}  # 0

user_dict.update({"name": input("Enter your name: ")})  # 1

user_dict.update({"age": int(input("Enter your age: "))})   # 2

user_dict.update({"fav_films": input("Enter your favourite films: ").split(",")})   # 3

print(user_dict)    # 4

print(list(user_dict.keys()))   # 5

key_to_change = input("Which key you want to change?: ")    # 6

value_to_change = input("Enter a value: ")  # 7

user_dict.update({key_to_change: value_to_change})  # 8

print(user_dict)    # 9

key_to_find = input("Enter a key you want to find: ")   # 10

key_not_found = input("What if there is no such key?: ")    # 11

print(user_dict.get(key_to_find, key_not_found))    # 12
