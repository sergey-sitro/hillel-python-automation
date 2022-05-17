x = "global"
# z = "glb"

def outer():
    x = "local"

    def inner():
        nonlocal x
        # nonlocal z
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)
