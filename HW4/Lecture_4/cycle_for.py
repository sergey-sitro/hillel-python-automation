lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i)


for i in range(100):
    print(i)
    if i == 10:
        break
    print("let's try next")


for i in range(20):
    print(i)
    if i % 10 == 0:
        print("some cool functionality")
        continue
    print("let's try next")


for i in range(5):
    print(i)
else:
    print(i)


for i in []:
    print(i)
else:
    print("excute in any case")


for i in range(5):
    for j in range(5, 10):
        print(i, j)
