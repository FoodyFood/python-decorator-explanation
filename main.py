print ("Decorating A Function Manually")

# Create our decorator function
def my_decorator_0(func): # This actually gets called during decoration, returning 'wrapper', now whatever you decorated is now a function pointer to 'wrapper' which has access to the say_hello funciton pointer
    print(f"Decorating {func.__name__}")
    def wrapper(): # This is a new function the decorator creates
        print(f"Calling function: {func.__name__}")
        func()  # Call the original function
        print(f"Function {func.__name__} finished execution.")
    return wrapper # This returns the 'wrapper' function

# Create the function we want to decorate
def say_hello_0():
    print("Hello, world!")

# Now we manually decorate our function
# We pass our function to the decorator
# The decorator then returns a pointer to the new wrapper function, which we overwrite our function with
say_hello_0 = my_decorator_0(say_hello_0)

# Our function now calls wrapper which internally calls the original say_hello_0
say_hello_0()


print("Decorate A Function Using A Decorator")
def my_decorator_1(func):
    print(f"Decorating {func.__name__}")
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Function {func.__name__} finished execution.")
    return wrapper

# The decorator gets called during decoration because of how the @decorator syntax works in Python
# Equivalent to having this line right after the function definition: my_function = my_decorator(my_function)
# The decorator is called immediately during the decoration step because Python needs to modify or replace
# the function with the decorated version before it is executed.
@my_decorator_1
def say_hello_1():
    print("Hello, world!")

say_hello_1()
