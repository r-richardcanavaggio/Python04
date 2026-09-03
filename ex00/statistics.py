from typing import Any


def compute_mean(*args: float | int) -> float:
    """Compute the arithmetic mean of given numbers."""
    if not args:
        raise ValueError("One number required for mean computation")

    return sum(args) / len(args)


def compute_median(*args: float | int) -> float:
    """Compute the median of given numbers."""
    if not args:
        raise ValueError("At least one number required"
                         "for median computation")

    numbers = sorted(args)
    n = len(numbers)
    mid = n // 2

    if n % 2 != 0:
        return float(numbers[mid])
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2.0


def compute_quartile(*args: float | int) -> list[float]:
    """Compute the 25% and 75% quartiles of given numbers."""
    if len(args) < 2:
        raise ValueError("At least two numbers required"
                         "for quartiles computation")

    numbers = sorted(args)
    n = len(numbers)
    mid = n // 2

    first = compute_median(*numbers[:mid])
    start_second_half = mid + 1 if n % 2 != 0 else mid
    last = compute_median(*numbers[start_second_half:])
    return [first, last]


def compute_var(*args: float | int) -> float:
    """Compute the variance of given numbers."""
    if not args:
        raise ValueError("At least one number required"
                         "for variance computation")

    mean = compute_mean(*args)

    return sum((x - mean) ** 2 for x in args) / len(args)


def compute_std(*args: float | int) -> float:
    """Compute the standard deviation of given numbers."""
    return compute_var(*args) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute and display requested statistical operations."""
    functions = {
        "mean": compute_mean,
        "median": compute_median,
        "quartile": compute_quartile,
        "var": compute_var,
        "std": compute_std,
    }

    for key, value in kwargs.items():
        func = functions.get(value)

        if func is not None:
            try:
                res = func(*args)
                print(f"{value} : {res}")
            except Exception:
                print("ERROR")
