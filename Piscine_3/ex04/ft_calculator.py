class calculator:
    """Calculator class for vector operations"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product of two vectors"""

        result = sum([x * y for x, y in zip(V1, V2)])
        print(f"Dot product is : {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two vectors"""

        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts two vectors"""

        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous vector is : {result}")


def main():
    try:
        V1 = [1.0, 2.0, 3.0]
        V2 = [4.0, 5.0, 6.0]

        print(f"Vector 1: {V1}")
        print(f"Vector 2: {V2}")

        calculator.dotproduct(V1, V2)
        calculator.add_vec(V1, V2)
        calculator.sous_vec(V1, V2)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
