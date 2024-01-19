import requests


class Employee:
    """A sample Employee class."""

    RAISE_FACTOR = 1.05

    def __init__(self, first: str, last: str, pay: float) -> None:
        """Initialize an Employee instance."""
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self) -> str:
        """Get the employee's email address."""
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property
    def fullname(self) -> str:
        """Get the employee's full name."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """Apply a raise to the employee's salary."""
        self.pay = int(self.pay * self.RAISE_FACTOR)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
