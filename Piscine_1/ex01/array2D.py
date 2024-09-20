from colorama import Fore, init

init(autoreset=True)


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array based on the provided start and end indices
    Args:
        family (list): A 2D array
        start (int): The start index for slicing
        end (int): The end index for slicing
    Returns:
        list: A 2D array sliced from the original array
    """

    if not isinstance(family, list):
        raise TypeError(Fore.RED + "The family parameter must be a list")

    are_all_rows_lists = all(isinstance(row, list) for row in family)
    row_lenghts = [len(row) for row in family]
    are_same_lenght = len(set(row_lenghts)) == 1

    if not are_all_rows_lists or not are_same_lenght:
        raise ValueError(Fore.RED + "Elements must be lists of the same size")

    shape = len(family), len(family[0])
    print(f"My shape is : {shape}")

    sliced_array = family[start:end]

    new_shape = (
        len(sliced_array), len(sliced_array[0])) if sliced_array else (0, 0)
    print(f"My new shape is : {new_shape}")

    return sliced_array


def main():
    print(Fore.CYAN + slice_me.__doc__)
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
