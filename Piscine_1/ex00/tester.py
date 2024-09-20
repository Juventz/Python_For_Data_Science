from give_bmi import give_bmi, apply_limit
from colorama import Fore, init

init(autoreset=True)


def test_cases():
    # Test case 1: Valid input
    try:
        height = [1.71, 1.55, 1.82]
        weight = [65.3, 50.4, 100.7]
        bmi = give_bmi(height, weight)
        print(Fore.GREEN + "Test case 1: Valid input")
        print("BMI values:", bmi)
        print("Apply limit (limit = 26):", apply_limit(bmi, 26))
    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)

    print("\n" + "-"*50 + "\n")

    # Test case 2: Different length lists
    try:
        height = [1.71, 1.55]
        weight = [65.3, 50.4, 100.7]
        print(Fore.GREEN + "Test case 2: Different length lists")
        bmi = give_bmi(height, weight)
    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)

    print("\n" + "-"*50 + "\n")

    # Test case 3: Invalid data type (non-numeric value in the height list)
    try:
        height = [1.71, "1.55", 1.82]
        weight = [65.3, 50.4, 100.7]
        print(Fore.GREEN + "Test case 3: Non-numeric value in height list")
        bmi = give_bmi(height, weight)
    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)

    print("\n" + "-"*50 + "\n")

    # Test case 4: Negative or zero value in height
    try:
        height = [1.71, 0, 1.82]
        weight = [65.3, 50.4, 100.7]
        print(Fore.GREEN + "Test case 4: Zero or negative value in height")
        bmi = give_bmi(height, weight)
    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)

    print("\n" + "-"*50 + "\n")

    # Test case 5: Invalid limit type in apply_limit
    try:
        height = [1.71, 1.55, 1.82]
        weight = [65.3, 50.4, 100.7]
        bmi = give_bmi(height, weight)
        print(Fore.GREEN + "Test case 5: Invalid limit type in apply_limit")
        print("Apply limit with a string:", apply_limit(bmi, "26"))
    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)

    print("\n" + "-"*50 + "\n")

    # Test case 6: Mixed int and float values
    try:
        height = [1.71, 155, 1.82]
        weight = [65, 50.4, 100]
        print(Fore.GREEN + "Test case 6: Mixed int and float values")
        bmi = give_bmi(height, weight)
        print("BMI values:", bmi)
        print("Apply limit (limit = 26):", apply_limit(bmi, 26))
    except Exception as e:
        print(Fore.RED + type(e).__name__ + ":", e)


if __name__ == "__main__":
    test_cases()
