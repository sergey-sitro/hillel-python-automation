def recursor():
    recursor()
recursor()


def factorial(x):
    print(x)
    if x == 1:
        print("returning 1")
        return 1
    else:
        print("go deeper")
        calc = factorial(x-1)
        print(calc)
        return x * calc


num = 3
print(f"The factorial of {num} is {factorial(num)}")




def booooooooom(i, j=1):
    if j > i:
        return
    yield j
    yield from booooooooom(i, j + 1)

for i in booooooooom(50):
    print(i)
