from S1E9 import Character
from colorama import Fore, init

init(autoreset=True)


class Baratheon(Character):
    """Represents the Baratheon family member"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the Baratheon family member"""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Represents the character's death"""

        self.is_alive = False

    def __str__(self):
        """Returns a string representation of the Baratheon family member"""

        return (f"Vector: ('{self.family_name}',\
'{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Returns a string representation of the Baratheon family member"""

        return (f"Vector: ('{self.family_name}',\
'{self.eyes}', '{self.hairs}')")


class Lannister(Character):
    """Represents the Lannister family member"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the Lannister family member"""

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Represents the character's death"""

        self.is_alive = False

    def __str__(self):
        """Returns a string representation of the Lannister family member"""

        return (f"Vector: ('{self.family_name}',\
'{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Returns a string representation of the Lannister family member"""

        return (f"Vector: ('{self.family_name}',\
'{self.eyes}', '{self.hairs}')")

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a Lannister member."""

        return cls(first_name, is_alive)


def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__},\
Alive : {Jaine.is_alive}")
        return

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
