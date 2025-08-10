
from collections import UserDict

contacts = {}

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # Я не зрозумів, як можна реалізувати цей класс
    # Сподіваюсь, що ви уточните 
    pass
        

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone in self.phones:
            return "Phone already exists"
        self.phones.append(Phone(phone))
        return f"Phone {phone} added for {self.name.value}."

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return f"Phone {old_phone} replaced by {new_phone}."
        return "Phone not found."

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Phone {phone} is deleted."
        return "Phone not found."

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"{self.name.value}: {', '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} removed."
        return "Contact not found."
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())