from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey
from matplotlib import pyplot as plt
from colorama import Fore, init

init(autoreset=True)


def test_main():
    print(Fore.CYAN + ft_invert.__doc__)
    try:
        image_path = "landscape.jpg"
        image = ft_load(image_path)

        if image is None:
            return
        print(image)

        inverted_image = ft_invert(image)
        red_image = ft_red(image)
        green_image = ft_green(image)
        blue_image = ft_blue(image)
        grey_image = ft_grey(image)

        filtered_images = [image, inverted_image, red_image,
                           green_image, blue_image, grey_image]
        titles = ["Original Image", "Inverted Image", "Red Image",
                  "Green Image", "Blue Image", "Grey Image"]

        for i, img in enumerate(filtered_images):
            plt.subplot(2, 3, i + 1)
            plt.imshow(img)
            plt.title(titles[i])
            plt.axis("off")

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
        print(Fore.YELLOW + "All images have been displayed")


if __name__ == "__main__":
    try:
        test_main()
    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
