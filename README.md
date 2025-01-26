# Python Decorators

An explanation and breakdown of decorators in python, how they work, and what we might use them for.


## What Is Decorating

Decorating a function essentially wraps it, allowing us to add code that runs before and after the function runs.


## When Would I Use A Decorator

Decorators are useful when we have many functions where we want to run some code both before and after their execution.

Simple example: [simple_examples_with_comments.py](./simple_examples_with_comments.py)

A good use could be for performance monitoring or measurement of the execution time of the function

You could print the time the function starts and the time it completes, allowing easy calculation of how long the function took to run.

Performance decorator example: [performance_monitoring_using_a_decorator.py](./performance_monitoring_using_a_decorator.py)

## Using A Decorator (Example)

Here we will create two functions that print a statement.

We want to add code before and after the function runs.


### Before Decorating

#### Code

```python
def our_function():
    print("Doing something cool")

def our_other_function():
    print("Doing another cool thing")

our_function()
our_other_function()
```

#### Result

```
Doing something cool
Doing another cool thing
```


### After Decorating

#### Code

```python
def our_decorator(func):
    def wrapper():
        print("I'm about to do something cool")
        func()
        print("I did something cool")
    return wrapper

@our_decorator
def our_function():
    print("Doing something cool")

@our_decorator
def our_other_function():
    print("Doing another cool thing")

our_function()

our_other_function()
```

#### Result

```
I'm about to do something cool
Doing something cool
I did something cool
I'm about to do something cool
Doing another cool thing
I did something cool

```

The code in our decorator was run before and after each of our decorated functions.


### How A Decorator Works

#### The Function

    You create a function with the name `my_function` that does something interesting.

#### Decoration

    You decorate the function using a decorator.

    At decoration, a pointer to `my_function` is passed to decorator function as a
    parameter.

    The decorator function stores a copy of the `my_function` pointer.

    The decorator creates a new function (called wrapper in the examples, but can be
    any name).

    The decorator returns a pointer to the new function it created.

    Your function `my_function` is then updated to point to the new function the
    decorator created.

    When you call `my_function`, it now calls the function that was created by the
    decorator.

#### Calling Your Function

    Now we call `my_function()`.

    Instead of starting the `my_function` code, it starts the new function that the
    decorator created.

    The function the decorator created has the copy of the pointer to the original
    `my_function` that was stored earlier.

    It starts `my_function` using that pointer, then returns.

    However, it allows you to add code before and after it starts `my_function`, this
    is the value that a decorator adds.


## Examples

### Example 1 - Simple Example With Comments

There are two examples in [simple_examples_with_comments.py](./simple_examples_with_comments.py.py), one where we 'manually' decorate a function, and one were we use the decorator correctly.

#### Result

If we run the simple examples we will get an output similar to:

```
Decorating A Function Manually
Decorating say_hello_0
Calling function: say_hello_0
Hello, world!
Function say_hello_0 finished execution.

Decorate A Function Using A Decorator
Decorating say_hello_1
Calling function: say_hello_1
Hello, world!
Function say_hello_1 finished execution.
```

### Example 2 - Performance Monitor

A more practical example has been provided in [performance_monitoring_using_a_decorator.py](./performance_monitoring_using_a_decorator.py) where we use a decorator to measure how long some functions take to execute.

#### Result

If we run the example we will get an output similar to:

```
Execution Time: 3.003030 seconds
Execution Time: 5.004452 seconds
```


## Improvements Or Notes

Please reach out if there are any improvements I could make.

