# Python Decorator Explanation

An explanation and breakdown of decorators in python, how they work, any why we might use one.


### Step By Step Explanation

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

However, you can add code before and after it starts `my_function`, this is the functionality that a decorator adds.

