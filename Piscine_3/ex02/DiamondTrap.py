from S1E7 import Baratheon, Lannister
from colorama import Fore, init

init(autoreset=True)


class King(Baratheon, Lannister):
    """Represents the false King of the seven kingdoms
    Inherits from Baratheon and Lannister"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the false King of the seven kingdoms"""
        Baratheon.__init__(self, first_name, is_alive)

    def get_eyes(self):
        """Returns the eye color of the false King"""
        return self.eyes

    def set_eyes(self, color: str):
        """Sets the eye color of the false King"""
        self.eyes = color

    def get_hairs(self):
        """Returns the hair color of the false King"""
        return self.hairs

    def set_hairs(self, color: str):
        """Sets the hair color of the false King"""
        self.hairs = color


def main():
    try:
        king = King("Robert")
        print(king)
        print(Fore.GREEN + f"King's eyes: {king.get_eyes()}")
        print(Fore.GREEN + f"King's hair: {king.get_hairs()}")

        king.set_eyes("green")
        king.set_hairs("blond")

        print(Fore.GREEN + f"King's eyes: {king.get_eyes()}")
        print(Fore.GREEN + f"King's hair: {king.get_hairs()}")

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
