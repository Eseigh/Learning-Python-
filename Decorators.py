def mydecorator(fn):
    def inner_function():
        fn()
        print('How are you?')
    return inner_function

@mydecorator
def greet():
    print('Hello! ')

greet()


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(3,0)

# Define the decorator functions
def make_bold(fn):
    def makebold_wrapped():
        return "<b>" + fn() + "</b>"

    return makebold_wrapped

def make_italic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"

    return makeitalic_wrapped

# Apply decorators to function hello
@make_bold
@make_italic
def hello():
    return 'hello world'

# Call function hello 
print(hello())
# Decorators with parameters in Python
def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):
        print("Inside inner function")
        print("I like", kwargs['like'])
        return func

    return inner

@decorator(like="python programming")
def func():
    print("Inside actual function")

func()



