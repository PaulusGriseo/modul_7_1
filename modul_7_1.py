import sys
import logging
from faker import Faker

fake = Faker('pl_PL')

logging.basicConfig(level=logging.INFO)

class BaseContact:
    def __init__(self, name, surname, phone, email_address) -> None:
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email_address = email_address

        self._label_lenth = 0

    def contact(self):
        info = ("Kontaktuję się z ->")
        result = print(f"{info} {self.name} {self.surname}; {self.phone}; {self.email_address}")
    
    def label_length(self):
        value = len(self.name)+len(self.surname)+1
        self._label_length = value
        print(f"Suma znaków imienia i nzwiska to: {value}")
        return self._label_length

class BussinesContact(BaseContact):
    def __init__(self, bussines_phone, company, job, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.bussines_phone = bussines_phone

    def contact(self):
        info = ("Kontaktuję się biznesowo z ->")
        result = print(f"{info} {self.name} {self.surname}; {self.company}; {self.job}; {self.bussines_phone}; {self.email_address}")

def create_contacts(aspect, quantity):
    if aspect == "base":
        for card in range(quantity):
            card = BaseContact(name:=fake.first_name(), surname:=fake.last_name(), phone:=fake.phone_number(), email_address:=fake.email())
            logging.info(f"{card.contact()}")
            logging.info(f"{card.label_length()}")
            
    elif aspect == "bussines":
        for card in range(quantity):
            card = BussinesContact(company:=fake.company(),job:=fake.job(), bussines_phone:=fake.phone_number(), name:=fake.first_name(), surname:=fake.last_name(), phone:=fake.phone_number(), email_address:=fake.email())
            logging.info(f"{card.contact()}")
            logging.info(f"{card.label_length()}")
            
    return card


contact_type = "bussines" 
contact_numbers = 5

create_contacts(contact_type, contact_numbers)