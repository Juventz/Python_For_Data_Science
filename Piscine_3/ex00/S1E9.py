from colorama import Fore, init
from abc import ABC, abstractmethod

init(autoreset=True)


class Character(ABC):
    """Represents a character in the story with a first name
    and a status of being alive"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the character with a first
        name and a status of being alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Represents the character's death """
        pass


class Stark(Character):
    """Represents a Stark family member """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the Stark family member """
        super().__init__(first_name, is_alive)

    def die(self):
        """Represents the character's death """
        self.is_alive = False


def main():

    print(Fore.CYAN + Character.__doc__)
    print(Fore.CYAN + Stark.__doc__)
    arya = Stark("Arya")
    print(f"{Fore.GREEN}{arya.first_name} is alive: {arya.is_alive}")
    arya.die()
    print(f"{Fore.RED}{arya.first_name} is alive: {arya.is_alive}")
    return


if __name__ == "__main__":
    main()
