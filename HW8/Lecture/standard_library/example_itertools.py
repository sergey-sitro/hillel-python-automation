import operator
import itertools
# https://docs.python.org/3/library/itertools.html

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(data)
print("---"*20)
print(f"list(itertools.accumulate(data, operator.mul)) - {list(itertools.accumulate(data, operator.mul))}")
print("---"*20)
print(f"list(itertools.accumulate(data, max)) - {list(itertools.accumulate(data, max))}")
print("---"*20)

print(f"list(itertools.chain(\"ABC\", \"DEF\")) - {list(itertools.chain('ABC', 'DEF'))}")
print("---"*20)
print(f"list(itertools.combinations(\"ABCD\", 2)) - {list(itertools.combinations('ABCD', 2))}")
print("---"*20)
