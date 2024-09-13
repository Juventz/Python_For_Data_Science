from sys import argv


def main():
    try:
        if len(argv) == 1:
            raise AssertionError("no argument is provided")
        elif len(argv) > 2:
            raise AssertionError("more than one argument is provided")

        # Get the argument
        arg = argv[1]

        try:
            # Attempt to convert the argument to an integer
            number = int(arg)
        except ValueError:
            # If conversion fails, print an error message
            raise AssertionError("argument is not an integer")

        # Check if the number is odd or even
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
