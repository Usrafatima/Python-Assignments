class A:
    def show(self):
        print("Show method in A")

class B(A):
    def show(self):
        print("Show method in B")

class C(A):
    def show(self):
        print("Show method in C")

class D(B, C):
    pass

d = D()
d.show()

print("MRO:", [cls.__name__ for cls in D.__mro__])
