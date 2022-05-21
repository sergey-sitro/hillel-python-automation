import json
# https://docs.python.org/3/library/json.html
dumps = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(dumps, type(dumps))

loads = json.loads(dumps)
print(loads, type(loads))