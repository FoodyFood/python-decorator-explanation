print ("Decorating A Function Manually")

# Create our decorator function
def my_decorator_2(func): # This actually gets called during decoration, returning 'wrapper', now whatever you decorated is now a function pointer to 'wrapper' which has access to the say_hello funciton pointer
    print(f"Decorating {func.__name__}")
    def wrapper(): # This appears to be a closure, we're creating a new function that has access to the function pointer from outside
        print(f"Calling function: {func.__name__}")
        func()  # Call the original function
        print(f"Function {func.__name__} finished execution.")
    return wrapper # This really returns 'wrapper' instead of 'say_hello, but wrapper has the function pointer inside it that get's called when you call wrapper

# Create the function we want to decorate
def say_hello_2():
    print("Hello, world!")

# Now we manually decorate our function
# We pass our function to the decorator
# The decorator then returns a pointer to the new wrapper function, which we overwrite our function with
say_hello_2 = my_decorator_2(say_hello_2)

# Our function name now calls wrapper
say_hello_2()



print("Decorate A Function Using A Decorator")
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
