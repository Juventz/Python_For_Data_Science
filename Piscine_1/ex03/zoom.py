from load_image import ft_load
from colorama import Fore, init
from matplotlib import pyplot as plt

init(autoreset=True)


def ft_zoom(image, start_x, end_x, start_y, end_y):
    """
    Zooms into the image based on the provided coordinates
    Args:
        image (np.array): The image to zoom into
        start_x (int): The starting x coordinate
        end_x (int): The ending x coordinate
        start_y (int): The starting y coordinate
        end_y (int): The ending y coordinate
    Returns:
        np.array: The zoomed image
    """
    return image[start_y:end_y, start_x:end_x]


def main():
    print(Fore.CYAN + ft_zoom.__doc__)

    image_path = "animal.jpeg"
    image = ft_load(image_path)

    if image is None:
        return

    print(f"The shape of the image is: {image.shape}")
    print(image)

    start_x, end_x = 400, 800
    start_y, end_y = 200, 600

    try:
        zoomed_image = ft_zoom(image, start_x, end_x, start_y, end_y)
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)

        plt.imshow(zoomed_image)
        plt.title("Zoomed Raccoon")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.gcf().canvas.manager.set_window_title("Zoomed Raccoon Head")

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
        print(Fore.YELLOW + "The zoomed image has been displayed")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "KeyboardInterrupt: Program has been terminated")
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
