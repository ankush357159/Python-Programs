class A(object):
    def __init__(self, something):
        print(self.something)
        self.something = something

class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print(self.something)
        self.something = something


# obj = B("something")

class Tweet:
    def __init__(self):
        print("Hello")
        # print(message)

    def printTweet(self, count):
        print("Nice to meet you")


a = Tweet()
a.printTweet("count")
# print(a)