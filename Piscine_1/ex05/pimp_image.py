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
    red_image = array * [1, 0, 0]

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

    # Set the red and green channels to 0
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
    green_image = array - ft_red(array) - ft_blue(array)

    return green_image


def ft_grey(array) -> np.array:
    """
    Keeps only the green channel of the image
    Args:
        array (np.array): The image to turn grey
    Returns:
        np.array: The grey image
    """
    grey_image = np.copy(array)

    # Calculate the mean of the RGB channels
    grey_value = np.mean(array, axis=2)

    # Set the RGB channels to the mean value
    grey_image[:, :, 0] = grey_value
    grey_image[:, :, 1] = grey_value
    grey_image[:, :, 2] = grey_value

    return grey_image
