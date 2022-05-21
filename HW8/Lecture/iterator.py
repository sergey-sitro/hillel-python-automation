class Iterator(object):
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.item = 1

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            self.item *= 2
            return self.item
        else:
            raise StopIteration


class Example(object):
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return Iterator(self.limit)


class ExampleExtra(object):
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.item = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            self.item *= 2
            return self.item
        else:
            raise StopIteration

example_extra = ExampleExtra(5)

example = Example(5)

for i in example:
    print(i)


