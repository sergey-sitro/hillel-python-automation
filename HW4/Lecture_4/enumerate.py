lst = ["a", "c", "test", 123, [], None]
for i, val in enumerate(lst):
    print(i, val)

for i, val in enumerate(lst, 10):
    print(i, val)
