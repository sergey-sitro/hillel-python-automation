# raise Exception


# user_input = input("Type all you want, but 'example': ")
# if user_input == "example":
#     raise Exception("No more examples!")
# print(user_input)


user_string = input("Type your string: ")
user_number = input(f"Tow many times to repeat '{user_string}': ")  # text 10 -10 --10
if not user_number.lstrip("-").isdigit():
    raise TypeError(f"You typed {user_number}, but it's not a number.")
try:
    user_number = int(user_number)
except ValueError as e:
    print("How it's happened?")
    # user_number = int(user_number.replace("-", ""))
    raise e
print(user_string * user_number)



# try:
#     print(1/0)
# except Exception as e:
#     raise RuntimeError("Ups...")

try:
    print(1/int(input("Type number: ")))
except Exception as e:
    raise RuntimeError("Ups...") from e
