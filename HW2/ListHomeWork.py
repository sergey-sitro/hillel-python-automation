# Exercise 1: Reverse a given list in Python
# aLsit = [100, 200, 300, 400, 500]
# Expected output:
# [500, 400, 300, 200, 100]

aLsit = [100, 200, 300, 400, 500]
aLsit.reverse()
print(aLsit)


# Exercise 2: Concatenate two lists index-wise
# Given:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:
# ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []

for i, j in zip(list1, list2):
    result.append(i+j)

print(result)


# Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
# Given:
# aList = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]

aList = [1, 2, 3, 4, 5, 6, 7]
aList = [i**2 for i in aList]
print(aList)


# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i+j)

print(list3)


# Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
# Given
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print(i, j)

# Exercise 6: Add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)
