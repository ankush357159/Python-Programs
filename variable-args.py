def myFunc1(*args):
    for arg in args:
        print(arg)

# myFunc1('Hello', 'hope', 'you', 'are','doing', 'well!')


def myFunc2(arg1, *args):
    print(arg1)
    for arg in args:
        print(arg)

# myFunc2('Hello', 'hope', 'you', 'are','doing', 'well!')

def myFunc3(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s" %(key,value))

# myFunc3(first="Hello", second="how", third="are you")

def myFunc4(*args, **kwargs):
    for arg in args:
        print(arg)
    for  key, value in kwargs.items():
        print("%s => %s" %(key,value))


myFunc4('This', 'is', 'true', first="Python", second="is", third="amazing")