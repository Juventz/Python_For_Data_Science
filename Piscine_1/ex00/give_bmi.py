def give_bmi(
        height: list[int | float], weight: list[int | float]) -> list[float]:
    """
    Calculates the BMI of a person based on their height and weight.
    Args:
    height: A list of integers or floats representing
    the height of a person in cm.
    weight: A list of integers or floats representing
    the weight of a person in kg.
    Returns:
    A list of floats representing the BMI of a person.
    """
    if height != weight:
        raise ValueError("Lenght of height and weight should be same")
    bmi = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("Height and weight should be integers or floats")
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight should be positive")

        bmi.append(w / ((h / 100) ** 2))

        return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if the BMI of a person is above a certain limit.
    Args:
    bmi: A list of integers or floats representing the BMI of a person.
    limit: An integer representing the upper limit of the BMI.
    Returns:
    A list of bool representing whether the BMI of a person is above the limit.
    """
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit should be an integer or float")

    return [b > limit for b in bmi]
