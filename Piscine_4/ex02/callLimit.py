def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called.
    """

    # This is the decorator function that will be called
    # The function is the function that will be decorated and limited
    # It returns a function that will be called instead of the original
    # Wrapping the original function
    def callLimiter(function):
        """Internal decorator function that limits the number
        of times a function can be called."""
        count = 0

        def limit_function(*args, **kwargs):
            """The actual function that will be called
            instead of the original and enforce the call limit."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


def main():
    print(callLimit.__doc__)

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
    g()


if __name__ == "__main__":
    main()
