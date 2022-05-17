x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)





x = "global"

def foo():
    print(x)
    x = 2

def foo():
    x += 2
    # global x
    # x = x + 2

foo()


# NEWER
var = []
def foo(arg):
    var.append(arg)
print(var)
foo(1)
foo(2)
foo(3)
print(var)
###


def foo():
    y = "local"
    print(y)


foo()
print(y)




z = "global "

def foo():
    global z
    y = "local"
    z = z * 2
    print(z)
    print(y)

foo()
print(z)




z = 5

def foo():
    z = 10
    print("local z:", z)


foo()
print("global z:", z)

