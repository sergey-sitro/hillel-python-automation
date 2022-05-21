import copy
# https://docs.python.org/3/library/copy.html

a = [1, 2, 3, 4]
b = a
print("b = a")
print("a is // == b")
print(a is b)
print(a == b)
c = copy.copy(a)
print("c copy a")
print("a is // == c")
print(a is c)
print(a == c)

a = [[1,2], [3, 4]]
b = copy.copy(a)
print("b copy a")
print("a is // == b")
print(a is b)
print(a == b)
print("a[0] is // == b[0]")
print(a[0] is b[0])
print(a[0] == b[0])
c = copy.deepcopy(a)
print("b deepcopy a")
print("a is // == c")
print(a is c)
print(a == c)
print("a[0] is // == c[0]")
print(a[0] is c[0])
print(a[0] == c[0])
