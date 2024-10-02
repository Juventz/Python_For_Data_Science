from colorama import Fore, init

init(autoreset=True)


class calculator:
    """Calculator ckass to perform operations with a vector and a scalar"""
    def __init__(self, vector):
        """Intializes the calculator (floats)"""
        self.vector = vector

    def __add__(self, scalar: float):
        """Adds a scalar to the vector"""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, scalar: float):
        """Subtracts a scalar from the vector"""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, scalar: float):
        """Multiplies the vector by a scalar"""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, scalar: float):
        """Divides the vector by a scalar"""
        if scalar == 0:
            raise ZeroDivisionError("division by zero")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
        return self.vector


def main():
    try:
        calc = calculator([1.0, 2.0, 3.0])
        print(Fore.GREEN + f"Initial vector: {calc.vector}")

        print(Fore.GREEN + f"Adding 2.0: {calc + 2.0}")
        print(Fore.GREEN + f"Subtracting 1.0: {calc - 1.0}")
        print(Fore.GREEN + f"Multiplying by 3.0: {calc * 3.0}")
        print(Fore.GREEN + f"Dividing by 2.0: {calc / 0}")

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
