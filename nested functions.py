# Why nest functions?
# Want to use a process a number of times within a function...
# Takes 3 numbers as parameters and performs the same function on each of them.
# writing out computation 3 times does not scale
# Define inner function within function definition


def mod2plus5(x1, x2, x3):
    """Return the raminder plus 5 of three values"""
    def inner(x):
        """Returns the reminder plus 5 of a value"""
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))


print(mod2plus5(1, 2, 3))


def raise_val(n):
    """Return the inner function."""
    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised
    return inner


square = raise_val(2)
cube = raise_val(3)

print(square(2), cube(4))


def outer():
    """Prints the value of n."""
    n = 1

    def inner():
        nonlocal n
        n = 2
        print(n)
    inner()
    print(n)


outer()
