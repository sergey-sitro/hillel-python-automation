summarize = lambda a, b: a + b
print(summarize(1, 2))
print(summarize(b="1", a="2"))

a = lambda: "Hello!"
print(a())
a = lambda: print("Hello!")
a()

a = lambda a, b=None, /, c=None, *args, d, e=None, **kwargs: None

example_list = list({"0": 10, "1": 15, "2": 5, "3": 0, "4": 20}.items())
print(example_list)
example_list.sort(key=lambda i: i[1])
print(example_list)


def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, range(100))))

print(list(filter(lambda i: i % 2 == 0, range(100))))


def square(x):
    return x ** 2

print(list(map(square, range(100))))

print(list(map(lambda i: i ** 2, range(100))))


from functools import reduce

print(reduce(lambda total, val: total * val, range(1, 10)))

