import json
import os


"""
Ця програма, представлена у вигляді консольного додатку, може бути встановлена як пакет
і викликатися у терміналі за допомогою команди 'hello'. Дані з роботи програми зберігаються
у файлі формата '.json' наприкінці роботи. При повторних викликах дані знов беруться з пам'яті комп'ютера.
"""


def input_error(func):
    """
    Декоратор, що обробляє можливі помилки, які можуть завчасно зупинити роботу програми
    """
    def inner(contacts: dict, command: list) -> bool:
        if func.__name__ == "end_script":
            try:
                if func(contacts, command) is False:
                    raise IndexError
            except IndexError:
                print("Leaving so soon? Type in: 'exit', 'good bye' or 'close'.")
            else:
                return True
        elif func.__name__ == "show_all":
            try:
                if func(contacts, command) is True:
                    raise IndexError
            except IndexError:
                print("Show what, exactly?")
        elif func.__name__ == "change_contact":
            try:
                if func(contacts, command) is False:
                    raise KeyError
            except KeyError:
                print("Insufficient data provided or contact doesn't exist.")
        elif func.__name__ == "add_contact":
            try:
                if func(contacts, command) is False:
                    raise KeyError
            except KeyError:
                print("Insufficient data provided or contact already exists.")
        elif func.__name__ == "get_phone":
            try:
                func(contacts, command)
            except KeyError:
                print("This person is not on your contact list.")
            except IndexError:
                print("Enter a name of the person whose number you require.")
        else:
            func(contacts, command)
        return False
    return inner


@input_error
def greet_again(contacts: dict, command: list) -> None:  # Повторне вітання
    print("Yes, hello again...")


@input_error
def change_contact(contacts: dict, command: list) -> bool:  # Змінити номер контакту. Сповістити якщо такого не існує
    name = command[1:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if not name or not contacts.get(name, None) or len(command) < 3:
        return False
    contacts[name] = command[-1]
    return True


@input_error
def get_phone(contacts: dict, command: list) -> None:  # Вивести на екран номер введеного контакту
    if command[1]:
        pass
    name = command[1:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    print(f"{name}: {contacts[name]}")


@input_error
def show_all(contacts: dict, command: list) -> bool:  # Показати всі записані контакти і їх номери
    if command[1].lower() == "all" and len(command) == 2:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        return False
    else:
        return True


@input_error
def end_script(contacts: dict, command: list) -> bool:  # Завершити роботу додатку
    if len(command) == 1 and command[0] != "good":
        print("Goodbye!")
        return True
    elif len(command) == 2 and command[1].lower() == "bye":
        print("Goodbye!")
        return True
    return False


@input_error
def nothing(contacts: dict, command: list) -> None:  # При введенні невідомої команди
    print("Unknown command.")


@input_error
def add_contact(contacts: dict, command: list) -> bool:  # Додати новий контакт. Сповістити якщо вже існує
    name = command[1:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if not name or contacts.get(name, None) or len(command) < 3:
        return False
    contacts[name] = command[-1]
    return True


def parser(command: list):  # Парсер команд. Видає відповідну хендлер-функцію
    execution = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "exit": end_script,
        "show": show_all,
        "close": end_script,
        "good": end_script,
        "hello": greet_again
    }
    return execution.get(command[0].lower(), nothing)


def main():  # Основна логіка програми
    directory_path = os.path.dirname(os.path.abspath(__file__))  # Шлях до директорії, в якій знаходиться програма
    storage_path = os.path.join(directory_path, "dict.json")  # Шлях до файлу, де будуть зберігатися дані
    if os.path.exists(storage_path):  # Перевірка чи існує вже файл для зберігання словника
        with open(storage_path, "r") as fh:  # Якщо файл існує - беремо дані з нього
            contacts = json.load(fh)
    else:  # Якщо файла не існує - створюємо новий словник
        contacts = {}
    print("How can I help you?")
    while True:  # Нескінченний цикл, який приймає команду і видає результат роботи
        command = input()
        if not command:
            continue
        command = command.split()
        if parser(command)(contacts, command):
            break
    with open(storage_path, "w") as fh:  # Зберігає словник з даними у файл. Збереження відбувається в останню чергу
        j = json.dumps(contacts)
        fh.write(j)


if __name__ == "__main__":
    main()
