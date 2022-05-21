def foo():
    yield 1
    yield 2
    yield 4

for i in foo():
    print(i)

a = foo()
next(a)
next(a)
next(a)
next(a)


def inf(to):
    n = 0
    while to >= n:
        yield n
        n += 1

print(sum(inf(10)))


def double(*args):
    for i in args:
        yield i * 2


print( list( double( *inf(10) ) ) )
print( list( (i * 2 for i in inf(10) ) ) )


def foo():
    for i in range(10):
        yield i
        if i == 3:
            return 1000


for i in foo():
    print(i)
a = foo()
next(a)
next(a)
next(a)
next(a)



def foo(*args):
    for i in args:
        yield i

def bar(itarable_1, iterable_2):
    yield from foo(*itarable_1)
    yield from foo(*iterable_2)
    for i in foo(*itarable_1):
        yield i

for i in bar(range(10), range(50, 60)):
    print(i)
