print("0") # Real decorator

def my_decorator_0(func):
    print(f"Decorating {func.__name__}")
    def wrapper():
        func()  # Call the original function
    return wrapper

@my_decorator_0
def say_hello_0():
    print("Hello, world!")

say_hello_0()



print("\n1") # Not a real decorator

def say_hello_1():
    print("Hello, world!")

def my_decorator_1(func): # This really only returns the same function it was passed
    print(f"Not decorating, just returning function pointer {func.__name__}")
    return func

my_decorator_1(say_hello_1)() # The decorator returns the function it was passed, then we execute it



print("\n2") # Real decorator, manually decorated

def my_decorator_2(func): # This actually gets called during decoration, returning 'wrapper', now whatever you decorated is now a function pointer to 'wrapper' which has access to the say_hello funciton pointer
    print(f"Decorating {func.__name__}")
    def wrapper(): # This appears to be a closure, we're creating a new function that has access to the function pointer from outside
        print(f"Calling function: {func.__name__}")
        func()  # Call the original function
        print(f"Function {func.__name__} finished execution.")
    return wrapper # This really returns 'wrapper' instead of 'say_hello, but wrapper has the function pointer inside it that get's called when you call wrapper

def say_hello_2():
    print("Hello, world!")

say_hello_2 = my_decorator_2(say_hello_2) # This is us decorating, it returns a function pointer to wrapper which we overwrite our variable contents with

say_hello_2() # this now calls wrapper

# We are creating a function
# We then pass a pointer to that function to the decorator, which returns a function pointer to wrapper, wrapper has the original pointer value stores
# We then call the function pointer to wrapper, wrapper then calls the stored function pointer to the function we wrapped



print("\n3") # Real decorator, correctly decorated

def my_decorator_3(func): # This actually gets called during decoration, returning 'wrapper', now whatever you decorated is now a function pointer to 'wrapper' which has access to the say_hello funciton pointer
    print(f"Decorating {func.__name__}")
    def wrapper(): # This appears to be a closure, we're creating a new function that has access to the function pointer from outside
        print(f"Calling function: {func.__name__}")
        func()  # Call the original function
        print(f"Function {func.__name__} finished execution.")
    return wrapper # This really returns 'wrapper' instead of 'say_hello, but wrapper has the function pointer inside it that get's called when you call wrapper

# The decorator gets called during decoration because of how the @decorator syntax works in Python. Let's break this down in detail.
# Equivalent to having this line right after the function definition: my_function = my_decorator(my_function)
# The decorator is called immediately during the decoration step because Python needs to modify or replace the function with the decorated version before it is executed.
@my_decorator_3
def say_hello_3():
    print("Hello, world!")

say_hello_3() # this calls wrapper which internally calls the original say_hello_3
