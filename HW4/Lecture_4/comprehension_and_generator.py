from datetime import datetime


lst = [i ** 2 for i in range(10)]
print(lst)

set_example = {i ** 2 for i in range(10)}
print(set_example)


lst = ["key_1", "key_2", "key_3", "key_4"]
dict_example = {key: value for value, key in enumerate(lst)}
print(dict_example)



lst = [i ** 2 for i in range(100) if i % 3 == 0]
print(lst)


tuple_example = (i ** 2 for i in range(10))
print(tuple_example)
next(tuple_example)


gen = lst.__iter__()
next(gen)


start = datetime.now()
a = [i for i in range(10000000)]
end = datetime.now()
print(end - start)


start = datetime.now()
a = (i for i in range(10000000))
end = datetime.now()
print(end - start)
