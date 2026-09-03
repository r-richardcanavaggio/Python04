import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def generate_login(self):
        self.login = self.name[0] + self.surname

    def generate_id(self):
        self.id = generate_id()

    def __post_init__(self):
        self.generate_login()
        self.generate_id()
