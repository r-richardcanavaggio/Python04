from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    mean = kwargs.get('mean', None)
    median = kwargs.get('median', None)
    quartile = kwargs.get('quartile', None)
    std = kwargs.get('std', None)
    var = kwargs.get('var', None)

    for key, value in kwargs.items():
        if (value == 'mean'):
            num = 0
            for i in range(len(args)):
                num = args[i] + num
            num = num / len(args)
            print(f"mean : {num}")
        elif value == 'median':
            new = sorted(args)
            print(new)
            res = 0
            if len(new) % 2 != 0:
                p = int((len(new) + 1) / 2)
                res = new[p - 1]
            else:
                p = int(len(new) / 2) - 1
                res = (new[p] + new[p + 1]) / 2
            print(res)
        