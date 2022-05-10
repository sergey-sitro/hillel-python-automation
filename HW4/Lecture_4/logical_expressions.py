x = 0
if x == 0:
    x += 1
print(x)


x = 0
if x == 0:
    x += 1
else:
    x -= 1
print(x)



x = 0
if x == 0:
    x += 1
elif x == 1:
    x -= 1
print(x)



x = 0
if x == 0:
    x += 1
elif x == 1:
    x -= 1
else:
    x = None
print(x)



if True:
    print("it's True")
elif not True:
    print("it's not True")
elif False:
    print("and it's not True")
else:
    print("hmmmm....")



val_1 = 0
val_2 = 3
val_3 = -5

if val_1 > val_2:
    pass
elif val_3 < val_1 < val_2:
    print("same: elif val_3 < val_1 and val_1 < val_2")
    if val_3 == val_2 * val_1 - 5:
        print("some calc")


val = 3
lst = [1, 2, 3, 4]
if val in lst:
    print("3 in list")
elif 5 not in range(5):
    print("ignored")
elif "bad" in "some good words":
    print("also ignored")


val_1 = "test"
val_2 = "new test"
val_3 = val_1 or val_2
print(val_3)
val_3 = "" or val_2
print(val_3)


val_1 = 10
val_2 = 0
val_3 = False

print("lazy")
print(val_3 and val_1 / val_2)


def foo(x):
    print(f"fuction returns {x}")
    return x

if foo(False):
    pass
elif foo(5) > foo(5) and foo(True):
    pass


a = [1, 2, 3]
b = a
c = [1, 2, 3]

if a is b:
    print(f"same obj with id's {id(a)} and {id(b)}")
if a is not c and a == c:
    print(f"dif obj with id's {id(a)} and {id(c)}")


a = 10 if True else 20
print(a)

a = 10 if False else 20 if False else 30 if True else 40
print(a)