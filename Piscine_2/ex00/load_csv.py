from colorama import Fore, init
from os import access, R_OK
import pandas as pd
from re import match

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

        data.fillna(0, inplace=True)

        if 'country' not in data.columns:
            print(Fore.RED + 'The column "country" is missing')
            return None

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
            if not pd.api.types.is_numeric_dtype(data[year]):
                print(Fore.RED + f"The column {year} is not numeric")
                return None

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


def main():
    print(Fore.CYAN + load.__doc__)
    print(load("life_expectancy_years.csv"))


if __name__ == '__main__':
    main()
