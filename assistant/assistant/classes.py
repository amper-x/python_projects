from collections import UserDict


class AddressBook(UserDict):
    """
    Об'єкт, що ітерує за атрибутами іншого об'єкта та створює з них словник.

    def add_record(self, record):
        for a in dir(record):
            if not a.startswith("__") and not callable(getattr(record, a)):
                tmp = f"self.data[a] = record.{a}"
                exec(tmp)

    """
    def add_record(self, name):
        self.data[name] = Record(name)


class Record:
    """
    Об'єкт, що зберігає в собі всю інформацію про контакт. При декларації приймає обов'язковий клас 'Name'.
    Має методи для додавання та редагування необов'язкового атрибута 'Phone'.
    """
    def __init__(self, name, phone=None, email=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.emails = [Email(email)] if email else []

    def add_phone(self, phone):  # Додати новий телефон
        for i in self.phones:
            if phone == i.value:
                return
        self.phones.append(Phone(phone))

    def del_phone(self, phone):  # Видалити існуючий телефон
        for i in self.phones:
            if phone == i.value:
                self.phones.remove(i)

    def change_phone(self, phone, new_phone):  # Замінити старий телефон на новий
        for i in self.phones:
            if phone == i.value:
                self.phones.remove(i)
                self.phones.append(Phone(new_phone))

    def add_email(self, email):  # Поки не реалізований функціонал
        for i in self.emails:
            if email == i.value:
                return
        self.emails.append(Email(email))

    def del_email(self, email):
        for i in self.emails:
            if email == i.value:
                self.emails.remove(i)

    def change_email(self, email, new_email):
        for i in self.emails:
            if email == i.value:
                self.emails.remove(i)
                self.emails.append(Email(new_email))


class Field:  # Батьківський клас для всіх полів
    def __init__(self, value):
        self.value = value


class Name(Field):  # Поки функціоналу батьківського класу вистачає, нам не треба уточнень
    pass


class Phone(Field):
    pass


class Email(Field):
    pass
