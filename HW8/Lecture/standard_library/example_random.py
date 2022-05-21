import random
# https://docs.python.org/3/library/random.html


print(f"random.randrange(start, stop[, step]) - {random.randrange(0, 10, 2)}")
print(f"random.randrange(start, stop[, step]) - {random.randrange(0, 10, 2)}")
print(f"random.randrange(start, stop[, step]) - {random.randrange(0, 10, 2)}")
print("---"*20)
print(f"random.randint(a, b) - {random.randint(0, 10)}")
print(f"random.randint(a, b) - {random.randint(0, 10)}")
print("---"*20)
print(f"random.choice(seq) - {random.choice(['a', 1, None, True, [5, 6]])}")
print(f"random.choice(seq) - {random.choice(['a', 1, None, True, [5, 6]])}")
print(f"random.choice(seq) - {random.choice(['a', 1, None, True, [5, 6]])}")
print("---"*20)
a = list(range(10))
print(f"random.shuffle({a}) - ", end ="")
random.shuffle(a)
print(f"{a}")
print("---"*20)
print(f"random.random() - {random.random()}")
print(f"random.random() - {random.random()}")
print(f"random.random() - {random.random()}")
print("---"*20)

