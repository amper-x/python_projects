from collections import UserDict
import datetime
import re


class AddressBook(UserDict):
    """
    Об'єкт, що ітерує за атрибутами іншого об'єкта та створює з них словник.
    """
    def add_record(self, name):
        self.data[name] = Record(name)

    def iterator(self, n=1):
        output = []
        i = 0

        for elem in self.data.values():
            output.append(elem)
            i += 1
            if i == n:
                yield output
                output = []
                i = 0
        if output:
            yield output


class Record:
    """
    Об'єкт, що зберігає в собі всю інформацію про контакт. При декларації приймає обов'язковий клас 'Name'.
    Має методи для додавання та редагування необов'язкового атрибута 'Phone'.
    """
    def __init__(self, name, phone=None, birthday=None, email=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.emails = [Email(email)] if email else []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):  # Додати новий телефон
        if phone not in list(map(lambda x: x.value, self.phones)) and Phone(phone).value:
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

    def add_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)

    def days_to_birthday(self):
        today = datetime.date.today()
        if not self.birthday.value:
            return None
        delta = datetime.date(today.year, self.birthday.value.month, self.birthday.value.day) - today
        if delta.days < 0:
            delta = datetime.date(today.year + 1, self.birthday.value.month, self.birthday.value.day) - today
        return delta.days

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
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isdecimal():
            self.__value = new_value


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            return
        tmp = re.findall(r"(?<![1-9])\d{1,4}", new_value)
        try:
            self.__value = datetime.date(int(tmp[2]), int(tmp[1]), int(tmp[0]))
        except IndexError:
            print("Please enter a valid date format: day:month:year, day.month.year, etc.")
        except ValueError:
            print("Such a date doesn't exist.")

    def __repr__(self):
        if self.__value is None:
            return "No birthday recorded."
        else:
            return f"Day: {self.__value.day}, Month: {self.__value.month}, Year: {self.__value.year}"


class Email(Field):
    pass
