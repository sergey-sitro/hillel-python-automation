x = 1
def foo(x):
    z = 2
    print(locals())
    return x ** z

print(globals())
foo(x)
