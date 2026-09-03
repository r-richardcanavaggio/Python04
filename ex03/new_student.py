import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character string for student ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def generate_login(self):
        """Generate login from student name and surname."""
        self.login = self.name[0] + self.surname

    def generate_id(self):
        """Generate student ID."""
        self.id = generate_id()

    def __post_init__(self):
        """Initialize login and ID after instance creation."""
        self.generate_login()
        self.generate_id()
