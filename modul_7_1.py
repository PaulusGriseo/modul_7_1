import sys
from faker import Faker

fake = Faker('pl_PL')

class Person:
    def __init__(self, surname, name, company, job, email_address) -> None:
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = job
        self.email_address = email_address

        self._label_lenth = 0

    def contact(self):
        info = ("Kontaktuję się z ->")
        result = print(f"{info} {self.name} {self.surname}; {self.company}; {self.email_address}")

    @property
    def label_lenth(self):
        value = len(name)+len(surname)+1
        self._label_lenth = value
        print(f"Suma znaków imienia i nzwiska to: {value}")
        return self._label_lenth

for Card in range(1):
    Card = Person(name:=fake.last_name(), surname:=fake.first_name(), company:=fake.company(), job:=fake.job(), email_address:=fake.email())
    Card.contact()
    Card.label_lenth