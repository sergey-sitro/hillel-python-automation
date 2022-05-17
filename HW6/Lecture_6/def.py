def foo():
    pass

print(foo())
foo.example_arg = "ARG"
print(foo.example_arg)


def foo():
    return None

print(foo())

def foo(a):
    return bool(a)

to_bool = foo

print(foo("test"))
print(to_bool("test"))


def get_age(x):
    return x["age"]

users = [
    {"name": "Alex", "age": 30},
    {"name": "Marta", "age": 20},
    {"name": "Username", "age": 40},
    {"name": "Junior", "age": 10},
]

print(sorted(users, key=get_age))  # ***!!!


def summarize(a, b):
    return a + b

print(summarize(1, 2))
print(summarize("1", "2"))
print(summarize(b="1", a="2"))


def summarize(a, b, c=10):
    return a + b + c

print(summarize(1, 2))
print(summarize(1, 2, 3))


def summarize(*args):  # args = tuple()
    print(args)
    result = 0
    for i in args:
        result += i
    return result

print(summarize())
print(summarize(1))
print(summarize(1, 2))
print(summarize(1, 2, 3))

example_list = [1, 2, 3, 4, 5, 6, 7]
print(summarize(*example_list))


def print_example_list(first, second, third):
    print(f"Super line\nfirst word - {first}\nsecond word = {second}\nthird word - {third}")

print_example_list("first", "second", "third")
print_example_list(first="first", second="second", third="third")
print_example_list(second="second", first="first", third="third")
example_list = ["first", "second", "third"]
print_example_list(*example_list)
example_dict = {"first": "test", "second": "test_2", "third": "test_3"}
print_example_list(**example_dict)


def print_dict(**kwargs):  # dict()
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


print_dict(first="test", a=1, boom=[123, 5, True])
example_dict = {"first": "test", "second": "test_2", "third": "test_3"}
print_dict(**example_dict)

# NEWER
def do_not(a=[]):
    a.append("test")
    print(a)

do_not()
do_not()
do_not()
do_not([])
do_not()
###


def foo(a, g, f, b=1, /, r=1, c=None, *args, d, y, l, e=None, **kwargs):
    pass


def standard_arg(arg):
    print(arg)

standard_arg(2)
standard_arg(arg=2)

def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(2)
pos_only_arg(arg=2)

def kwd_only_arg(*, arg):
    print(arg)

kwd_only_arg(2)
kwd_only_arg(arg=2)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)
