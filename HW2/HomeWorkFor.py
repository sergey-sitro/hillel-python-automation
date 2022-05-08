# Exercise 1: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Note: You can use more than 1 “for” statement. Also if you put “\n” into the string, line break will appear. See https://www.w3schools.com/python/gloss_python_escape_characters.asp for more info about the escape symbols.


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Exercise 2: Print multiplication table of a given number
# For example, num = 2 so the output should be
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


number = int(input('Input a number to print multiplication table: '))

for n in range(1, 11):
    print(number * n)


# Exercise 3: Print the following pattern using for loop
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1

for i in range(5, 0, -1):
    for j in range(i, 0, - 1):
        print(j, end=" ")
    print()


# Exercise 4: Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10


list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)


# Exercise 5: Display numbers from -10 to -1 using for loop
# Expected output:
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10, 0):
    print(i)


# Exercise 6: Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Note: you can not only to include one “for” into another but also use several of them in your program


for i in range(0, 5):
    for j in range(0, i + 1):
        print('*', end=' ')
    print()

for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print('*', end=' ')
    print()
