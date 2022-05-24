class A:
    def a(self):
        print("a")

class AltA:
    def a(self):
        print("alt a")

class B:
    def b(self):
        print("b")

class AltB:
    def b(self):
        print("alt b")

class C:
    def c(self):
        print("c")

class AB(A, B):
    def ab(self):
        self.a()
        self.b()

class AltAB(AB):
    def ab(self):
        self.b()
        self.a()

class ABC(AB, C):
    def abc(self):
        self.ab()
        self.c()

class A_AltA_B(A, AltA, B):
    pass

class AltA_A_B(AltA, A, B):
    pass

class AltA_AB(AltA, AB):
    pass

class AltA_AltB_AltAB(AltA, AltB, AltAB):
    pass

A().a()
AltA().a()
B().b()
AltB().b()
C().c()
AB().a()
AB().b()
AB().ab()
AltAB().a()
AltAB().b()
AltAB().ab()
ABC().a()
ABC().b()
ABC().c()
ABC().ab()
ABC().abc()
A_AltA_B().a()
A_AltA_B().b()
AltA_A_B().a()
AltA_A_B().b()
AltA_AB().a()
AltA_AB().b()
AltA_AB().ab()
AltA_AltB_AltAB().a()
AltA_AltB_AltAB().b()
AltA_AltB_AltAB().ab()


print(AB.__mro__)
print(AltAB.__mro__)
print(ABC.__mro__)
print(A_AltA_B.__mro__)
print(AltA_A_B.__mro__)
print(AltA_AB.__mro__)
print(AltA_AltB_AltAB.__mro__)
