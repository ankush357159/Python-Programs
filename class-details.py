class A(object):
    def __init__(self, something):
        print(self.something)
        self.something = something

class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print(self.something)
        self.something = something


obj = B("something")