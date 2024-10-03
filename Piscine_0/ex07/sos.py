from sys import argv
from colorama import Fore, init

init(autoreset=True)

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def encode_morse(text: str) -> str:
    """
    Encode the given text into Morse Code.
    Args:
    - text (str): The input text to encode.
    Returns:
    - str: The Morse Code representation of the input text.
    """
    morse_code = []
    for char in text.upper():
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char])
        else:
            raise AssertionError(Fore.RED + "Character not supported.")
    return ' '.join(morse_code)


def main():
    try:
        # print(Fore.CYAN + encode_morse.__doc__)
        if len(argv) != 2:
            raise AssertionError(Fore.RED + "Usage: python sos.py <text>")

        text = argv[1]
        if not text:
            raise AssertionError(Fore.RED + "The text cannot be empty")

        print(encode_morse(text))

    # except AssertionError as e:
    #     print(Fore.RED + type(e).__name__ + ":", e)
    #     return

    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)
        return

    finally:
        print(Fore.YELLOW + "\nExecution completed.")


if __name__ == "__main__":
    main()
