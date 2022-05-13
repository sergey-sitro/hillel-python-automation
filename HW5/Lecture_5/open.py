file = open("example.txt", "w")
file.write('hello world !')
file.close()


file = open("example.txt", "w")
try:
    file.write('hello world !')
finally:
    file.close()


with open('example.txt', 'w') as file:
    file.write('hello world !')


with open('example.txt', 'w', encoding='utf-8') as file:
    line = input()
    print(line, file=file)

"""
open(file, mode='r')

r - read
w - write, remove all content form file
x - write, rice exception if file exists
a - write, append
b - in binary
t - in text
+ - read and write

file - path to file
"""

open("zen_python.txt", "x")


with open('zen_python.txt') as file:
    print(file.name)
    print(file.mode)
    print(file.closed)

    for line in file:
        print(line)
print(file.closed)


"""
.read(n=-1) - > all

.readline(limit=-1) - > line

.readlines() - > list of lines
"""

file = open('zen_python.txt')
print(file.read())
file.close()

file = open('zen_python.txt')
print(file.readline())
file.close()

file = open('zen_python.txt')
print(file.readlines())
file.close()

"""
.write(line)

.writelines()
"""

file = open("example.txt", "w")
file.write('hello world !')
file.close()

file = open("example.txt", "w")
lines_list = [f"{str(i**2)}\n" for i in range(200)]
file.writelines(lines_list)
file.close()

file = open("example.txt", "a")
lines_list = [f"{str(i**2)}\n" for i in range(200)]
file.writelines(lines_list)
file.close()


"""
.tell()

.seek()
"""

file = open('zen_python.txt')
position = file.tell()
print(position)
print(file.readline())
position = file.tell()
print(position)
print(file.readline())
position = file.tell()
print(position)
print("seek to 33")
file.seek(33)
print(file.readline())
print("seek to 33")
file.seek(33)
print(file.readline())
file.close()
