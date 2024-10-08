from dataclasses import dataclass, field
from random import choices
from string import ascii_lowercase


def generate_id() -> str:
    return "".join(choices(ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname}".capitalize()
