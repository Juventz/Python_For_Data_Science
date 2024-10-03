from colorama import Fore, init

init(autoreset=True)


def callLimit(limit: int):

    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwargs):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                raise Exception(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


