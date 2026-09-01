from typing import Any


def compute_mean(*args: float | int) -> float:
    if not args:
        raise ValueError("One number required for mean computation")

    return sum(args) / len(args)

def compute_median(*args: float | int) -> float:
    if not args:
        raise ValueError("One number required for median computation")

    numbers = sorted(args)
    n = len(numbers)
    mid = n // 2

    if n % 2 != 0:
        return float(numbers[mid])
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2.0

def compute_quartile(*args: float | int) -> list[float]:
    if len(args) < 2:
        raise ValueError("At least 2 numbers required for quartiles computation")

    numbers = sorted(args)
    n = len(numbers)
    mid = n // 2

    first = compute_median(*numbers[:mid])
    start_second_half = mid + 1 if n % 2 != 0 else mid
    last = compute_median(*numbers[start_second_half:])
    return [first, last]

functions = {
    "mean": compute_mean,
    "median": compute_median,
    "quartile": compute_quartile,
}

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for key, value in kwargs.items():
        func = functions.get(value)

        if func is not None:
            try:
                res = func(*args)
                print(f"{value} : {res}")
            except ValueError:
                print("ERROR")
