from colorama import Fore, init
from os import access, R_OK
import pandas as pd
from re import search, match

init(autoreset=True)


def convert_(value: str):
    """
    Convert a string to a float.
    Args:
        value (str): The string to convert.
    Returns:
        float: The converted value.
    """

    if isinstance(value, (int, float)):
        return value
    try:
        if search(r'\.\..*', value):
            raise ValueError(Fore.RED + f"Invalid value: {value}")
        if value.count('.') > 1:
            raise ValueError(Fore.RED + f"Invalid value: {value}")
        if value.count('k') > 1:
            raise ValueError(Fore.RED + f"Invalid value: {value}")
        if value.count('B') > 1:
            raise ValueError(Fore.RED + f"Invalid value: {value}")
        if value.count('M') > 1:
            raise ValueError(Fore.RED + f"Invalid value: {value}")
        if search(r'[a-zA-Z].*\d', value):
            raise ValueError(Fore.RED + f"Invalid value: {value}")

        if 'k' in value:
            if match(r'^\d+(\.\d+)?k$', value):
                return float(value.replace('k', '').replace(',', '').strip()) \
                    * 1000
            else:
                raise ValueError(Fore.RED + f"Invalid value: {value}")
        elif 'B' in value:
            if match(r'^\d+(\.\d+)?B$', value):
                return float(value.replace('B', '').replace(',', '').strip()) \
                    * 1000000000
            else:
                raise ValueError(Fore.RED + f"Invalid value: {value}")
        elif 'M' in value:
            if match(r'^\d+(\.\d+)?M$', value):
                return float(value.replace('M', '').replace(',', '').strip()) \
                    * 1000000
            else:
                raise ValueError(Fore.RED + f"Invalid value: {value}")
        else:
            return float(value.replace(',', '').strip())

    except ValueError:
        raise ValueError(Fore.RED + f"Could not convert {value} to a float")


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
        data.fillna(0, inplace=True)

        if 'country' not in data.columns:
            print(Fore.RED + 'The column "country" is missing')
            return None

        # Check if the column country contains invalid values
        invalid_country = data['country'].str.contains(r'\d', regex=True)
        if invalid_country.any():
            print(Fore.RED + f"The column country contains invalid values'\
                  {data['country'][invalid_country]}")
            return None

        year_columns = [col for col in data.columns if col != 'country']

        invalid_year = [year for year in year_columns
                        if not match(r'^\d+$', year)]
        if invalid_year:
            print(Fore.RED + f"The column(s) {invalid_year}\
                  contain(s) invalid values")
            return None

        for year in year_columns:
            try:
                data[year] = data[year].apply(convert_)
            except Exception as e:
                print(Fore.RED + f"{type(e).__name__}: {e}")
                return None

        print(Fore.YELLOW + f"Loading dataset of dimensions {data.shape}")

        return data

    except IOError:
        if not access(path, R_OK):
            print(Fore.RED + 'The file is not readable')
        else:
            print(Fore.RED + 'An error occurred while reading the file')
        return None

    except FileNotFoundError as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None
