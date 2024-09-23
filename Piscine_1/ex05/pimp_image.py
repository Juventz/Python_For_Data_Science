import numpy as np


def ft_invert(array) -> np.array:
    """
    Inverts the colors of the image
    Args:
        array (np.array): The image to invert
    Returns:
        np.array: The inverted image
    """
    inverted_image = 255 - array

    return inverted_image


def ft_red(array) -> np.array:
    """
    Keeps only the red channel of the image
    Args:
        array (np.array): The image to turn red
    Returns:
        np.array: The red image
    """
    red_image = np.copy(array)
    red_image[:, :, 1] = 0
    red_image[:, :, 2] = 0

    return red_image


def ft_blue(array) -> np.array:
    """
    Keeps only the blue channel of the image
    Args:
        array (np.array): The image to turn blue
    Returns:
        np.array: The blue image
    """
    blue_image = np.copy(array)
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0

    return blue_image


def ft_green(array) -> np.array:
    """
    Keeps only the green channel of the image
    Args:
        array (np.array): The image to turn green
    Returns:
        np.array: The green image
    """
    green_image = np.copy(array)
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0

    return green_image


def ft_grey(array) -> np.array:
    """
    Keeps only the green channel of the image
    Args:
        array (np.array): The image to turn grey
    Returns:
        np.array: The grey image
    """
    grey_image = np.mean(array, axis=2, dtype=np.int32)
    grey_image = grey_image.astype(np.uint8)

    grey_image = np.stack([grey_image] * 3, axis=-1)

    return grey_image
