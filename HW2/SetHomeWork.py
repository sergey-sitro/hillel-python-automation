# Exercise 1: Add a list of elements to a given set
# Given:
# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red"]
# Expected output:
# Note: Set is unordered.
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

sampleList = ["Blue", "Green", "Red"]
sampleSet = {"Yellow", "Orange", "Black"}

result = sampleSet.update(set(sampleList))

print(sampleSet)


# Exercise 2: Return a new set of identical items from a given two set
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}
#
# Note. Try “intersection” method of “set” object

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
print(set3)


# Exercise 3: Returns a new set with all items from both sets by removing duplicates
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 40, 10, 50, 20, 60, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# print(set(list(set1) + list(set2)))     # первое, что пришло в голову)))
print(set1.union(set2))


# Exercise 4: Given two Python sets, update the first set with items that exist only in the first set and not in the second set.
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# Expected output:
# set1 {10, 30}

set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))


# Exercise 5: Remove items 10, 20, 30 from the following set at once
# set1 = {10, 20, 30, 40, 50}
# Expected output:
# {40, 50}
#
# Note. Try to use “difference_update” method of “set” object.

set1 = {10, 20, 30, 40, 50}
items_to_discard = [10, 20, 30]

set1.difference_update(items_to_discard)

print(set1)


# Exercise 6: Return a set of all elements in either A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {20, 70, 10, 60}

# Note. Try “symmetric_difference” method of “set” object.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))
