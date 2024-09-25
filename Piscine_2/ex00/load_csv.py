from colorama import Fore, init
from os import access, R_OK
import pandas as pd

init(autoreset=True)


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return its content as a list of lists.
    Args:
        path (str): The path to the CSV file.
    Returns:
        list: The content of the CSV file as a list of lists
    """
    try:
        data = pd.read_csv(path)

        print(Fore.YELLOW + f"Loading dataset of dimensions {data.shape}")

        return data

    except IOError:
        if not access(path, R_OK):
            print(Fore.RED + 'The file is not readable')
        else:
            print(Fore.RED + 'An error occurred while reading the file')
        return None

    except FileNotFoundError:
        print(Fore.RED + 'File not found')
        return None

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None
