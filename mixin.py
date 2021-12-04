class A:
    total=1254

class B(A):
    pass

class C(A):
    pass

class M:
    def total_print(self):
        print(self.total)
        

class X(C,M):
    pass

class Y(B,M):
    pass

e = X()
e.total_print()

event = Y()
event.total_print()