with open('example.txt') as file:
    text = file.read().split()

with open("spam.txt", "w") as file:
    file.writelines(set(text))
