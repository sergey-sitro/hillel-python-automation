example_list = list(range(2, 10))

end = int(input("Slice end: "))
print(example_list[:end])

new_item = input("Extra list item: ")
example_list.append(new_item)
print(example_list)

print("Let's double it")
example_list.extend(example_list)
print(example_list)

print("Let's leave unique only")
example_set = set(example_list)
print(example_set)

users_words = input("Your favorite words (single only, use space): ")
users_words_list = users_words.split(" ")
print(users_words_list)
random_word = users_words_list[-1]
print(f"Wow! '{random_word.upper()}' - is my favorite word too! Will add it to your list.")
users_words_list.append(random_word)

print("Let's leave unique only")
users_words_list = list(set(users_words_list))
print(", ".join(users_words_list).title())

user_info = {}
pet_name = input("Your pet name: ")
user_info["pet_name"] = pet_name
print(user_info)
