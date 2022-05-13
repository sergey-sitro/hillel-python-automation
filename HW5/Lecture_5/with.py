try:
    print("start")
    raise Exception
finally:
    print("exit")


class Controller(object):
    def __enter__(self):
        print("__enter__ starts")
        return "example string"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with Controller() as ctrl:
    print("with starts")
    print(ctrl)
    raise Exception("exception raised")
