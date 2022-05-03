# Exercise
# 1: Reverse the following tuple
#
# aTuple = (10, 20, 30, 40, 50)
# Expected output:
#
# (50, 40, 30, 20, 10)
#
# Note: You can’t reverse tuple, but list you can.

aTuple = (10, 20, 30, 40, 50)
print(tuple(reversed(list(aTuple))))

# Exercise 2: Unpack the following tuple into 4 variables
# aTuple = (10, 20, 30, 40)
# Expected output:
#
# aTuple = (10, 20, 30, 40)
#
# # Your code
#
# print(a)  # should print 10
#
# print(b)  # should print 20
#
# print(c)  # should print 30
#
# print(d)  # should print 40
#
# Note: You can assign the tuple into several vars.
# tpl = 1, 2, 3
#
# x, y, z = tpl
#
# print(x)  # 1
# print(y)  # 2
# print(z)  # 3

aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple

print(a)
print(b)
print(c)
print(d)


# Exercise 3: Access value 20 from the following tuple
#
# aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
# Expected output:
#
# 20

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])


# Exercise 4: Create a tuple with single item 50

aTuple = (50,)
print(type(aTuple))


# Exercise 5: Swap the following two tuples
#
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# Expected output:
#
# tuple1 = (99, 88)
#
# tuple2 = (11, 22)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1

print(tuple1)
print(tuple2)


# Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
#
# tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:
#
# tuple2: (44, 55)

tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = (tuple1[3], tuple1[4])

print(tuple2)


# Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
#
# tuple1 = (11, [22, 33], 44, 55)
# Expected output:
#
# tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222

print(tuple1)


# Exercise 8: Counts the number of occurrences of item 50 from a tuple
#
# tuple1 = (50, 10, 60, 70, 50)
# Expected output:
#
# 2

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
