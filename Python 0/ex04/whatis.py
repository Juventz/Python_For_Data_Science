import sys

def main():
    if len(sys.argv) == 1:
        print("AssertionError: no argument is provided")
        return
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    
    # Get the argument
    arg = sys.argv[1]

    try:
        # Attempt to convert the argument to an integer
        number = int(arg)
    except ValueError:
        # If conversion fails, print an error message
        print("AssertionError: argument is not an integer")
        return
    
    # Check if the number is odd or even
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
