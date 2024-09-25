from colorama import Fore, init
import numpy as np

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

    if not all(isinstance(row, list) for row in family):
        raise ValueError(Fore.RED + "The family parameter must be a 2D array")

    for row in family:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(Fore.RED + "All elements must be int or float")

    row_lenght = [len(row) for row in family]
    if len(set(row_lenght)) != 1:
        raise ValueError(Fore.RED + "Elements must be lists of the same size")

    # Convert the list to a numpy array
    family_np = np.array(family)
    if family_np.ndim != 2:
        raise ValueError(Fore.RED + "The family parameter must be a 2D array")

    # Check if all the inner lists have the same length
    if len(set(len(row) for row in family)) != 1:
        raise ValueError(Fore.RED + "Elements must be lists of the same size")

    shape = family_np.shape
    print(f"My shape is : {shape}")

    sliced_array = family_np[start:end]
    new_shape = sliced_array.shape
    print(f"My new shape is : {new_shape}")

    return sliced_array.tolist()


def main():
    print(Fore.CYAN + slice_me.__doc__)
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
