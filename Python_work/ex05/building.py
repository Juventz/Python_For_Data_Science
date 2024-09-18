from sys import argv
import string
from colorama import Fore, init

init(autoreset=True)


def count_charact(text: str) -> None:

    """
    Count_Charact :
    Count the number of {} in the text:
    - number of character
    - number of uppercase character
    - number of lowercase character
    - number of punctuation character
    - number of whitespace character
    - number of digit

    Args: text (str): The text to count
    Returns: None
    """

    if not isinstance(text, str):
        raise TypeError("The input must be a string")

    num_chars = len(text)

    num_upper = sum(1 for c in text if c.isupper())

    num_lower = sum(1 for c in text if c.islower())

    num_punct = sum(1 for c in text if c in string.punctuation)

    num_whitespace = sum(1 for c in text if c.isspace())

    num_digits = sum(1 for c in text if c.isdigit())

    # Print the results
    print(f"The text contains {num_chars} characters:")
    print(f"{num_upper} upper letters")
    print(f"{num_lower} lower letters")
    print(f"{num_punct} punctuation marks")
    print(f"{num_whitespace} spaces")
    print(f"{num_digits} digits")


def main() -> None:
    try:
        print(Fore.CYAN + count_charact.__doc__)

        if len(argv) > 2:
            raise AssertionError(Fore.RED + "Usage: python building.py [text]")

        if len(argv) == 2 and argv[1] != "None":
            text = argv[1]
        else:
            text = input("What is the text to count?\n")

        count_charact(text)

    except AssertionError as e:
        print(Fore.RED + type(e).__name__ + ":", e)
        return

    except KeyboardInterrupt:
        print(Fore.RED + "Program interrupted by user using ctr + C")
        return

    except EOFError:
        print(Fore.RED + "EOFError: Program interrupted by user using ctr + D")
        return

    except TypeError as e:
        print(Fore.RED + type(e).__name__ + ":", e)
        return

    except ValueError:
        print(Fore.RED + "ValueError: The input must be a string")
        return

    except Exception:
        print(Fore.RED + "An unexpected error occured")
        return


if __name__ == "__main__":
    main()
