def foo(func):
    def wrapper():
        print("do smth 1")
        func()
        print("do smth 2")
    return wrapper


def hello():
    print("hello")

foo(hello)()

# hello = foo(hello)
# hello()

@foo
def hello():
    print("hello")

hello()



def timer(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@timer
def test():
    import requests
    requests.get("https://google.com/")

test()



def foo(func):
    def wrapper(a, b):
        print("do smth 1")
        result = func(a, b)
        print("do smth 2")
        return result
    return wrapper

def foo(func):
    def wrapper(x, y=10):
        try:
            return func(x, y)
        except ZeroDivisionError:
            return "Hahaha"
    return wrapper

@foo
def summarize(a, b):
    return a / b

print(summarize(1, 2))



def timer(func):
    import time
    def wrapper(url):
        start = time.time()
        result = func(url)
        end = time.time()
        print(end - start)
        print(result)
    return wrapper

@timer
def test(url):
    import requests
    requests.get(url)

test("https://google.com/")



def bread(func):
    def wrapper():
        print("Bread")
        func()
        print("Bread")
    return wrapper

def sauce(func):
    def wrapper():
        print("Sauce")
        func()
        print("Sauce")
    return wrapper

def cheese(func):
    def wrapper():
        print("Cheese")
        func()
        print("Cheese")
    return wrapper

@bread
@sauce
@cheese
def burger():
    print("Cutlet")

burger()


def decorator_factory(argument):
    import time
    def decorator(function):
        def wrapper(*args, **kwargs):
            total = 0.0
            for i in range(argument):
                start = time.time()
                result = function(*args, **kwargs)
                end = time.time()
                diff = end - start
                print(i, diff)
                total += end - start
            print(total / argument)
        return wrapper
    return decorator

@decorator_factory(10)
def test(url):
    import requests
    requests.get(url)

test("https://google.com/")
