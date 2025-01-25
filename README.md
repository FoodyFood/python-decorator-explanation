# Python Decorators

An explanation and breakdown of decorators in python, how they work, and what we might use them for.


## What Is Decorating

Decorating a function essentially wraps it, allowing us to add code before and after.


## When Would I Use A Decorator

Decorators are useful when we have many functions where we want to run some code both before and after their's execution.

A good use could be for performance monitoring or measurement of the execution time of the function.

You could print the time the function starts and the time it completes, allowing easy calculation of how long the function took to run.


## Using A Decorator (Example)

Here we will create two function that print a statement.

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

You create a function with the name `my_function` that does something interesting.

You decorate the function using a decorator.

At decoration, a pointer to `my_function` is passed to decorator function as a parameter.

The decorator function stores a copy of the pointer to `my_function`.

The decorator creates a new function (called wrapper in the examples, but can be any name).

The decorator returns a pointer to tbe new function it created.

Your function `my_function` is then updated to point to the new function the decorator created.

When you call `my_function`, it now calls the function that was created by the decorator.

Now we call `my_function()`.

Instead of starting the `my_function` code, it starts the new function that the decorator created.

The function the decorator created has the copy of the pointer to `my_function` that was stored earlier.

It starts `my_function` using that pointer, then returns.

However, you can add code before and after it starts `my_function`, this is the value that a decorator adds.


## Examples

There are two examples in [main.py](./main.py), one where we 'manually' decorate a function, and one were we use the decorator correctly.


## Improvements Or Notes

Please reach out if there are any improvements I could make.

