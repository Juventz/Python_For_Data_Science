from colorama import Fore, init

init(autoreset=True)


def ft_tqdm(lst: range) -> None:
    """
    This function provides a visual progress bar that updates in real-time
    as you iterate over the given range object. It uses the `yield` keyword
    to generate items from the input range while displaying the progress bar.

    Parameters:
    lst(range): a range obj representing the sequence of items to iterate over.
    This should be a valid range object, e.g., range(10) or range(1, 11).

    Raises:
    TypeError: If the provided argument is not a range object.
    """

    if not isinstance(lst, range):
        raise TypeError("ft_tqdm() argument must be a range object")

    total = len(lst)
    if total <= 0:
        raise ValueError("range object must have at least one element")
    bar_length = 40

    for i, elem in enumerate(lst):

        percentage = (i + 1) / total * 100

        filled_length = int(bar_length * (i + 1) // total)

        bar = f"{Fore.GREEN}{'█' * filled_length}{Fore.WHITE} \
{'█' * (bar_length - filled_length)}"

        print(f"\r{Fore.WHITE}{percentage:.2f}% \
|{bar}| {i + 1}/{total}", end="")

        yield elem

    print()
