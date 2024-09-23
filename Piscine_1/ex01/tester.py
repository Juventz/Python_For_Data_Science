from array2D import slice_me
from colorama import Fore, init

init(autoreset=True)


def main():
    # Valid test cases
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(Fore.LIGHTBLUE_EX + "Valid cases:")
    try:
        print("Case 1: Slicing from index 0 to 2")
        print(slice_me(family, 0, 2))  # Expected: [[1.80, 78.4],[2.15, 102.7]]

        print("\nCase 2: Slicing from index 1 to -2")
        print(slice_me(family, 1, -2))  # Expected: [[2.15, 102.7]]
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")

    print(Fore.LIGHTBLUE_EX + "\nInvalid cases:")

    # Case 1: Not a list
    try:
        print("Case 1: Passing a non-list input")
        print(slice_me("not a list", 0, 2))  # Expected: TypeError
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")

    # Case 2: Inner lists of different lengths
    try:
        print("\nCase 2: Passing a 2D array with different row lengths")
        invalid_family = [
            [1.80, 78.4],
            [2.15, 102.7, 50.0],  # This row has an extra element
            [2.10, 98.5]
        ]
        print(slice_me(invalid_family, 0, 2))  # Expected: ValueError
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")

    # Case 3: Negative start index
    try:
        print("\nCase 3: Passing a negative start index")
        print(slice_me(family, -3, 2))  # Expected: [[2.10, 98.5],[1.88, 75.2]]
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")

    # Case 4: Start index greater than end index
    try:
        print("\nCase 4: Passing a start index greater than end index")
        print(slice_me(family, 2, 1))  # Expected: []
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
