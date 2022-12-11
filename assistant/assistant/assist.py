import json
import os


"""
Ця програма, представлена у вигляді консольного додатку, може бути встановлена як пакет
і викликатися у терміналі за допомогою команди 'hello'. Дані з роботи програми зберігаються
у файлі формата '.json' наприкінці роботи. При повторних викликах дані знов беруться з пам'яті комп'ютера.
"""


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print('Name not on your contact list.')
        except ValueError as exception:
            print(f"{exception.args[0]}")
        except IndexError:
            print('Insufficient data.')
        except TypeError:
            print('Unknown command.')
    return inner


@input_error
def greet_again(command: list, contacts: dict) -> None:  # Повторне вітання
    print("Yes, hello again...")


@input_error
def change_contact(command: list, contacts: dict) -> None:  # Змінити номер контакту. Сповістити якщо такого не існує
    name = command[1:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if not len(name) or not command[-1].isdecimal():
        raise ValueError("Please enter the name and the phone.")
    elif name not in contacts:
        raise ValueError("This contact doesn't exist.")
    contacts[name] = command[-1]


@input_error
def add_contact(command: list, contacts: dict) -> None:  # Додати новий контакт. Сповістити якщо вже існує
    name = command[1:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if not len(name) or not command[-1].isdecimal():
        raise ValueError("Please enter the name and the phone.")
    elif name in contacts:
        raise ValueError("This contact already exists.")
    contacts[name] = command[-1]


@input_error
def get_phone(command: list, contacts: dict) -> None:  # Вивести на екран номер введеного контакту
    name = command[1:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    print(f"{name}: {contacts[name]}")


@input_error
def show_all(command: list, contacts: dict) -> None:  # Показати всі записані контакти і їх номери
    if command[1].lower() == "all" and len(command) == 2:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


@input_error
def end_script(command: list, contacts: dict) -> bool:  # Завершити роботу додатку
    if len(command) == 1 and command[0] != "good":
        print("Goodbye!")
    elif len(command) == 2 and command[1].lower() == "bye":
        print("Goodbye!")
    else:
        raise ValueError("Unknown command.")
    return True


def nothing(command: list, contacts: dict) -> None:
    print("Unknown command.")


@input_error
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
        if parser(command)(command, contacts):
            break
    with open(storage_path, "w") as fh:  # Зберігає словник з даними у файл. Збереження відбувається в останню чергу
        j = json.dumps(contacts)
        fh.write(j)


if __name__ == "__main__":
    main()
