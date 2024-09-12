import sys
import string


def count_charact(text: str) -> None:

    """
    Count the number of characters in the text:
    - number of characters
    - number of digits
    - number of whitespace characters
    - number of punctuation characters
    - number of lowercase characters
    - number of uppercase characters

    Args: text (str): The text to count
    Returns: None
    """

    # Count the number of characters in the text
    num_chars = len(text)

    # Count the number of digits in the text
    num_digits = sum(1 for c in text if c.isdigit())

    # Count the number of whitespace characters in the text
    num_whitespace = sum(1 for c in text if c.isspace())

    # Count the number of punctuation characters in the text
    num_punct = sum(1 for c in text if c in string.punctuation)

    # Count the number of lowercase characters in the text
    num_lower = sum(1 for c in text if c.islower())

    # Count the number of uppercase characters in the text
    num_upper = sum(1 for c in text if c.isupper())

    # Print the results
    print(f"The text contains {num_chars} characters:")
    print(f"{num_upper} upper letters")
    print(f"{num_lower} lower letters")
    print(f"{num_punct} punctuation marks")
    print(f"{num_whitespace} spaces")
    print(f"{num_digits} digits")


def main() -> None:

    # print(count_charact.__doc__)

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")

    count_charact(text)


if __name__ == "__main__":
    main()
