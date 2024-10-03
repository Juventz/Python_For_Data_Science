from colorama import Fore, init

init(autoreset=True)


def ft_mean(data: list):
    """This function calculates the mean of a list of numbers."""
    return sum(data) / len(data)


def ft_median(data):
    """This function calculates the median of a list of numbers."""
    data_sorted = sorted(data)

    n = len(data_sorted)
    mid = n // 2
    if n % 2 == 0:
        median_value = (data_sorted[mid - 1] + data_sorted[mid]) / 2
        return int(median_value) if median_value.is_integer() else median_value
    else:
        return int(data_sorted[mid]) if data_sorted[mid].is_integer()\
              else data_sorted[mid]


def ft_quartiles(data: list, n: int) -> list:
    """This function calculates the quartiles of a list of numbers."""
    data_sorted = sorted(data)
    q1 = data_sorted[int(len(data_sorted) / 4)]
    q3 = data_sorted[int(len(data_sorted) * 3 / 4)]
    return [q1, q3]


def ft_variance(data: list) -> float:
    """This function calculates the standard deviation of a list of numbers."""
    mean = ft_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_stdev(data):
    """This function calculates the standard deviation of a list of numbers."""
    var = ft_variance(data)
    return var ** 0.5


# kwargs : dict that contains the keyword arguments passed to the function
# args : tuple that contains the positional arguments passed to the function
def ft_statistics(*args: any, **kwargs: any):
    """
    This function calculates the mean, median, quartile,
    standard deviation, and variance of a list of numbers."""

    data = [float(arg) for arg in args if isinstance(arg, (int, float))]

    operations = {
        "mean": lambda x: ft_mean(x),
        "median": lambda x: ft_median(x),
        "quartile": lambda x: ft_quartiles(x, 4),
        "var": lambda x: ft_variance(x),
        "std": lambda x: ft_stdev(x),
    }

    if not data:
        for key, value in kwargs.items():
            print(Fore.RED + "ERROR")
        return None

    for key, value in kwargs.items():
        if value in operations:
            result = operations[value](data)
            if result is not None:
                print(Fore.GREEN + f"{value}: {result}")
            else:
                print(Fore.RED + "ERROR")

    return None


def main():
    print(Fore.CYAN + ft_statistics.__doc__)
    try:
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, mean="mean")
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, median="median")
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, quartile="quartile")
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, stdev="stdev")
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, variance="variance")
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, test="mean")
        ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, mean="test")
        ft_statistics()

    except Exception:
        print(Fore.RED + "ERROR")
        return


if __name__ == "__main__":
    main()
