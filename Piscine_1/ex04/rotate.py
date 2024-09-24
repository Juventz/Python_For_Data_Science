from load_image import ft_load
from colorama import Fore, init
from matplotlib import pyplot as plt
import numpy as np

init(autoreset=True)


def ft_rotate(image):
    """
    Rotates the image based on the provided angle
    Args:
        image (np.array): The image to rotate
    Returns:
        np.array: The rotated image
    """
    rows, cols = image.shape[:2]
    transposed = np.zeros((cols, rows, *image.shape[2:]), dtype=image.dtype)

    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = image[i, j]

    return transposed


def main():
    print(Fore.CYAN + ft_rotate.__doc__)

    image_path = "animal.jpeg"
    image = ft_load(image_path)

    if image is None:
        return

    print(f"The shape of the image is: {image.shape}")
    print(image)

    start_x, end_x = 400, 800
    start_y, end_y = 200, 600

    try:
        squared_image = image[start_y:end_y, start_x:end_x]
        # squared_image = ft_zoom(image, start_x, end_x, start_y, end_y)
        rotated_image = ft_rotate(squared_image)

        print(f"New shape after Transpose: {rotated_image.shape}")
        print(rotated_image)

        plt.imshow(rotated_image)
        plt.title("Rotated Raccoon")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.gcf().canvas.manager.set_window_title("Rotated Raccoon Head")

        try:
            plt.show()

        except Exception as e:
            print(Fore.RED + f"{type(e).__name__}: {e}")
            return

    except KeyboardInterrupt:
        print(Fore.RED + "KeyboardInterrupt: Program has been terminated")
        return

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return

    finally:
        plt.close()
        print(Fore.YELLOW + "The rotated image has been displayed")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "KeyboardInterrupt: Program has been terminated")
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
