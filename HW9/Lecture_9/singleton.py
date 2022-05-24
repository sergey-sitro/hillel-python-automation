class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        print("new")
        print(cls, args, kwargs)
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        print("init")
        print(self, args, kwargs)
        self.args = args
        self.kwargs = kwargs
        super().__init__()

a = Singleton(1)
b = Singleton(2)

print(a == b)
print(a is b)
print(a.args)
print(b.args)
