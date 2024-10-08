from dataclasses import dataclass, field
from random import choices
from string import ascii_lowercase


def generate_id() -> str:
    """Generate a random string of 15 lowercase letters."""
    return "".join(choices(ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __init__(self, name: str, surname: str, active: bool = True, **kwargs):
        try:
            if 'id' in kwargs:
                raise TypeError("Student.__init__() got an unexpected\
keyword argument 'id'")

            self.name = name
            self.surname = surname
            self.active = active
            self.login = f"{self.name[0]}{self.surname}".capitalize()

        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            exit(1)


def main():
    print(Student.__doc__)
    print(generate_id.__doc__)
    print("")
    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)


if __name__ == "__main__":
    main()
