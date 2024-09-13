from ft_filter import ft_filter
from sys import argv
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def main():
    try:

        # print donc ft_filter
        print(Fore.CYAN + ft_filter.__doc__)

        if len(argv) != 3:
            raise AssertionError(Fore.RED + "Usage: python filterstring.py \
<string> <number>")

        S = argv[1]

        try:
            N = int(argv[2])
        except ValueError:
            raise AssertionError(Fore.RED + "Arg[2] must be an integer")

        W = S.split()

        # remove all punction and special characters from W
        for word in W:
            if not word.isalnum():
                raise AssertionError(Fore.RED + "Characters not supported")

        # filter the words that have more than N characters
        result = ft_filter(lambda word: len(word) > N, W)

        print(result)

    except AssertionError as e:
        print(Fore.RED + type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()
