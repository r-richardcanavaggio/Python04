from typing import Any


def callLimit(limit: int):
    """Decorator factory that limits execution count of a function."""
    def callLimiter(function):
        """Wrap a function to limit its total number of calls."""
        count = 0

        def limit_function(*args: Any, **kwargs: Any):
            """Execute function if under limit, else display error message."""
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
