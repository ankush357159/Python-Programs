# Function as an object

def sample1(text):
    return text.upper()

print(sample1("How are you?"))

sample2 = sample1

print(sample2("I am fine"))


#Function passed to other function as argument
def shout(text):
    return text.lower()

def whisper(text):
    return text.upper()


def greet(func):
    greeting = func("""This is a testing text""")
    print(greeting)

greet(shout)
greet(whisper)