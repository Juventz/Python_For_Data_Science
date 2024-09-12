from ft_filter import ft_filter
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        # the input string
        S = sys.argv[1]

        try:
            # the number of characters to
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        W = S.split()

        # remove all punction and special characters from W
        for word in W:
            if not word.isalnum():
                raise AssertionError("the arguments are bad")

        # filter the words that have more than N characters
        result = ft_filter(lambda word: len(word) > N, W)

        print(result)

    except AssertionError as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()
