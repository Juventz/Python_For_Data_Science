from colorama import Fore, init

init(autoreset=True)


def give_bmi(
        height: list[int | float], weight: list[int | float]) -> list[float]:
    """
    Give_bmi :
    Calculates the BMI of a person based on their height and weight.
    Args:
    height: A list of integers or floats representing
    the height of a person in cm.
    weight: A list of integers or floats representing
    the weight of a person in kg.
    Returns:
    A list of floats representing the BMI of a person.
    """
    if len(height) != len(weight):
        raise ValueError(Fore.RED + "Lenght of height and weight do not match")

    bmi = []

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError(Fore.RED + "Height/weight should be int or float")
        if h <= 0 or w <= 0:
            raise ValueError(Fore.RED + "Height/weight should be positive")

        bmi.append(w / (h ** 2))

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply_limit :
    Checks if the BMI of a person is above a certain limit.
    Args:
    bmi: A list of integers or floats representing the BMI of a person.
    limit: An integer representing the upper limit of the BMI.
    Returns:
    A list of bool representing whether the BMI of a person is above the limit.
    """
    if not isinstance(limit, (int, float)):
        raise TypeError(Fore.RED + "Limit should be an integer or float")

    return [b > limit for b in bmi]


def main():

    print(Fore.CYAN + give_bmi.__doc__)
    print(Fore.CYAN + apply_limit.__doc__)

    try:
        height = [1.71, 1.55, 1.84]
        weight = [65.3, 50.4, 100.7]

        bmi = give_bmi(height, weight)

        print("The calculated BMI values:")
        print(bmi, type(bmi))

        print("\nResults of apply_limit (limit = 26):")
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
