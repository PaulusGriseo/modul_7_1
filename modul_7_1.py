import sys
from faker import Faker

fake = Faker('pl_PL')

#logging.basicConfig(level=logging.INFO)

private_contcts = []
bussines_contcts = []

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

    @property
    def label_lenth(self):
        value = len(name)+len(surname)+1
        self._label_lenth = value
        print(f"Suma znaków imienia i nzwiska to: {value}")
        return self._label_lenth

class BussinesContact(BaseContact):
    def __init__(self, bussines_phone, company, job, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.bussines_phone = bussines_phone


def create_contacts(aspect, quantity):
    if aspect == BaseContact:
        for contact in range(quantity):
            contact = aspect(name:=fake.first_name(), surname:=fake.last_name(),phone:=fake.phone_number(), email_address:=fake.email())
    elif aspect == BussinesContact:
        for contact in range(quantity):
            contact = aspect(name:=fake.last_name(), surname:=fake.first_name(),bussines_phone:=fake.phone_number(), email_address:=fake.email(), company:=fake.company(), job:=fake.job())
            
    
create_contacts(BaseContact, 10)
#create_contacts(BussinesContact, 10)


#Card.contact()
#Card.label_lenth