from classes import AddressBook, Record


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


def parser(command: list):  # Парсер команд. Видає відповідну хендлер-функцію
    execution = {
        "create": create_contact,
        "delete contact": delete_contact,
        "add number": add_number,
        "change number": change_number,
        "delete phone": delete_phone,
        "show phones": show_phones,
        "show all": show_all,
        "close": end_script,
        "exit": end_script,
        "good bye": end_script,
        "hello": greet_again,
        "add birthday": add_birthday,
        "birthday": show_birthday,
        "next birthday": days_to_birthday,
        "show part": show_part
    }
    tmp = " ".join(command[0:2])
    if tmp in execution.keys():
        return execution.get(tmp)
    return execution.get(command[0].lower(), nothing)


@input_error
def create_contact(command: list) -> None:
    name = command[1:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if name not in book.data.keys():
        book.add_record(name)
    else:
        pass


@input_error
def delete_contact(command: list) -> None:
    name = command[2:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    del book.data[name]


@input_error
def add_number(command: list) -> None:
    name = command[2:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    number = command[-1]
    book.data[name].add_phone(number)


@input_error
def change_number(command: list) -> None:
    name = command[2:-2]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    old, new = command[-2], command[-1]
    book.data[name].change_phone(old, new)


@input_error
def delete_phone(command: list) -> None:
    name = command[2:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    number = command[-1]
    book.data[name].del_phone(number)


@input_error
def show_phones(command: list) -> None:
    name = command[2:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    print(f"{name}: {[i.value for i in book.data[name].phones]}")


@input_error
def add_birthday(command: list) -> None:
    name = command[2:-1]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if not book.data[name].birthday.value:
        book.data[name].add_birthday(command[-1])
    else:
        print("This contact already has a birthday.")


@input_error
def show_birthday(command: list) -> None:
    name = command[1:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    if not book.data[name].birthday.value:
        print("This contact doesn't have a birthday.")
    else:
        print(book.data[name].birthday.value)


@input_error
def days_to_birthday(command: list) -> None:
    name = command[2:]
    for count, value in enumerate(name):
        name[count] = value.lower().capitalize()
    name = " ".join(name)
    print(f"Days to next birthday of {name} in {book.data[name].days_to_birthday()} days.")


@input_error
def show_all(command: list) -> None:
    for key, val in book.data.items():
        print(f"Name: {key}\nBirthday: {val.birthday}\nPhones: {[i.value for i in val.phones]}"
              f"\nEmails: {[i.value for i in val.emails]}")


@input_error
def show_part(command: list) -> None:
    n = command[-1]
    counter = 1
    for chunk in book.iterator(int(n)):
        print(f"\nChunk {counter}:\n")
        counter += 1
        for record in chunk:
            print(f"Name: {record.name.value}\nBirthday: {record.birthday}\nPhones: {[i.value for i in record.phones]}"
                  f"\nEmails: {[i.value for i in record.emails]}")


@input_error
def end_script(command: list) -> bool:
    print("Fare thee well...")
    return True


@input_error
def nothing(command: list) -> None:
    print("Invalid command.")


@input_error
def greet_again(command: list) -> None:  # Повторне вітання
    print("Greetings...")


def main():  # Основна логіка програми
    """
    Поки що видалив зберыгання в документі.
    """
    print("How can I help you?")
    while True:  # Нескінченний цикл, який приймає команду і видає результат роботи
        command = input()
        if not command:
            continue
        command = command.split()
        if parser(command)(command):
            break


if __name__ == "__main__":
    book = AddressBook()
    main()
