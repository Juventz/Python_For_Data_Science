from colorama import Fore, init
from PIL import Image
import numpy as np
from os import access, R_OK

init(autoreset=True)


def ft_load(path: str) -> np.array:
    """
    Loads an image from the provided path
    and returns it spiel in RGB format
    Args:
        path (str): The path to the image
    Returns:
        np.array: The image in RGB format
    """
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        img_array = np.array(img)

        print(f"The shape of Image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print(Fore.RED + f"The file '{path}' was not found")
        return None

    except IOError:
        if not access(path, R_OK):
            print(Fore.RED + f"The file '{path}' is not readable")
        else:
            print(Fore.RED + f"The file '{path}' is not a valid image file")
        return None

    except MemoryError:
        print(Fore.RED + "Memory Error: The image is too large")
        return None

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None


def main():
    print(Fore.CYAN + ft_load.__doc__)

    try:
        img = ft_load("Luffy.jpg")
        print(img)

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
