def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of a number by itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that repeatedly applies function to x."""
    count = 0

    def inner() -> float:
        """Apply function to x, update x, and return the new value."""
        nonlocal count
        nonlocal x

        count += 1
        x = function(x)
        return x

    return inner
