from colorama import init, Fore

init(autoreset=True)


def square(x: int | float) -> int | float:
    """This function takes an integer or float and returns the square of it.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """This function takes an integer or float and returns the power of it.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """This function takes an integer or float and returns the power of it.
    """
    count = 0

    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner


def main():
    try:
        x = float(input("Enter a number: "))
        print(Fore.GREEN + f"Square of {x} is {square(x)}")
        print(Fore.GREEN + f"Power of {x} is {pow(x)}")
        print(Fore.GREEN + f"Power of {x} is {outer(x)()}")

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
