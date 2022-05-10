index = 0
while index < 10:
    print(index)
    index += 1


index = 0
while index < 10:
    print(index)
    if index % 5 == 0 and index > 0:
        print(f"cycle stopped on {index}")
        break
    index += 1



index = 0
while index < 15:
    print(index)
    if index == 5:
        print(f"index is {index}. let's skip 5")
        index += 5
        continue
    index += 1


index = 0
while index < 10:
    print(index)
    index += 1
else:
    print(f"index less than 10")
