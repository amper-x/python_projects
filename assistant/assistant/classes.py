from collections import UserDict


class AddressBook(UserDict):
    """
    Об'єкт, що ітерує за атрибутами іншого об'єкта та створює з них словник.
    """
    def add_record(self, record):
        for a in dir(record):
            if not a.startswith("__") and not callable(getattr(record, a)):
                tmp = f"self.data[a] = record.{a}"
                exec(tmp)


class Record:
    """
    Об'єкт, що зберігає в собі всю інформацію про контакт. При декларації приймає обов'язковий клас 'Name'.
    Має методи для додавання та редагування необов'язкового атрибута 'Phone'.
    """
    def __init__(self, name):
        self.name = name.value
        self.phone = []
        self.email = []

    def add_phone(self, phone):  # Додати новий телефон
        if phone.value not in self.phone:
            self.phone.append(phone.value)

    def del_phone(self, phone):  # Видалити існуючий телефон
        if phone.value in self.phone:
            self.phone.remove(phone.value)

    def change_phone(self, phone, new_phone):  # Замінити старий телефон на новий
        if phone.value in self.phone:
            self.phone.remove(phone.value)
            self.phone.append(new_phone.value)

    def add_email(self, email):  # Поки не реалізований функціонал
        if email.value not in self.email:
            self.email.append(email.value)


class Field:  # Батьківський клас для всіх полів
    def __init__(self, value):
        self.value = value


class Name(Field):  # Поки функціоналу батьківського класу вистачає, нам не треба уточнень
    pass


class Phone(Field):
    pass
