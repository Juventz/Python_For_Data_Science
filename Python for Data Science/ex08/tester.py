from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
from colorama import Fore, init

init(autoreset=True)


# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()

# for elem in tqdm(range(-10, -1)):
#     sleep(0.005)
# print()


def test_ft_tqdm():
    print(Fore.GREEN + ft_tqdm.__doc__)
    try:
        print("1. Testing ft_tqdm with a valid range:")
        for elem in ft_tqdm(range(10)):
            sleep(0.1)
        print()

        print("2. Testing ft_tqdm with an empty range:")
        try:
            for elem in ft_tqdm(range(0)):
                sleep(0.1)
        except ValueError as e:
            print(f"Caught expected exception: {e}")
        print()

        print("3. Testing ft_tqdm with invalid input:")
        try:
            for elem in ft_tqdm("string"):
                sleep(0.1)
        except TypeError as e:
            print(f"Caught expected exception: {e}")
        print()

        print("4. Testing ft_tqdm with a negative range:")
        try:
            for elem in ft_tqdm(range(-10, -1)):
                sleep(0.1)
        except ValueError as e:
            print(f"Caught expected exception: {e}")
        print()

    except Exception as e:
        print(f"An unexpected exception occurred: {e}")


if __name__ == "__main__":
    test_ft_tqdm()
    print()

    # Test with tqdm for comparison
    for elem in tqdm(range(10)):
        sleep(0.1)
    print()
