from datetime import date, timedelta
import calendar


def main():
    """
    Ця функція існує лише для тестування програми. Викликає функцію 'get_birthdays_per_week()',
    підставляючи в неї список словників.
    """

    users = [{"name": "Aaron", "birthday": date(year=1995, month=1, day=1)},
             {"name": "Billy", "birthday": date(year=2000, month=1, day=3)},
             {"name": "Cass", "birthday": date(year=1995, month=12, day=31)},
             {"name": "Derek", "birthday": date(year=2000, month=12, day=30)},
             {"name": "Eugine", "birthday": date(year=1995, month=1, day=4)},
             {"name": "Frank", "birthday": date(year=2000, month=12, day=28)},
             {"name": "George", "birthday": date(year=1995, month=7, day=21)},
             {"name": "Howard", "birthday": date(year=2000, month=12, day=30)},
             {"name": "Ian", "birthday": date(year=1995, month=9, day=25)},
             {"name": "James", "birthday": date(year=2000, month=10, day=23)},
             {"name": "Karen", "birthday": date(year=1995, month=11, day=13)},
             {"name": "Larry", "birthday": date(year=2000, month=12, day=14)},
             {"name": "Monika", "birthday": date(year=1995, month=11, day=16)},
             {"name": "Nigel", "birthday": date(year=2000, month=11, day=16)},
             {"name": "Olivia", "birthday": date(year=1995, month=11, day=15)},
             {"name": "Peter", "birthday": date(year=2000, month=11, day=17)},
             {"name": "Quentin", "birthday": date(year=1995, month=1, day=1)},
             {"name": "Robert", "birthday": date(year=2000, month=2, day=17)},
             {"name": "Sierra", "birthday": date(year=1995, month=3, day=3)},
             {"name": "Tyler", "birthday": date(year=2000, month=4, day=9)},
             {"name": "Utah", "birthday": date(year=1995, month=5, day=5)},
             {"name": "Voldemar", "birthday": date(year=2000, month=6, day=7)},
             {"name": "Wottard", "birthday": date(year=1995, month=7, day=22)},
             {"name": "Xarxes", "birthday": date(year=2000, month=8, day=11)},
             {"name": "Yulia", "birthday": date(year=1995, month=9, day=30)},
             {"name": "Zacharius", "birthday": date(year=2000, month=11, day=17)}]

    get_birthdays_per_week(users)


def get_birthdays_per_week(users):
    """
    Функція приймає список словників із даними співробітників.
    Виводить на екран список людей, яких необхідно привітати з днем народження наступного тижня. Враховує
    дні народження на вихідних поточного тижня, записуючи їх на понеділок.
    """
    if not users:  # Перевіряє чи був наданий аргумент
        print("No input was given.")
    # Створюємо словник з ключами, що відповідають дням тижня і значеннями - коли треба привітати людей
    b_day_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Monday", 6: "Monday"}
    current_date = date.today()
    print(f"Current day: {calendar.day_name[current_date.weekday()]}\nListing the birthdays for the upcoming week:")
    iterator = []  # Зберігаємо об'єкти date, які відповідають дням на наступному тижні і двом вихідним цього тижня
    if current_date.weekday() == 6:  # Перевірка на те, якщо поточний день - 'Неділя'
        iterator.append(current_date - timedelta(days=1))
        iterator.append(current_date)
        current_date += timedelta(days=1)

    while len(iterator) < 7:  # Додаємо об'єкти до списку. Список починається з суботи (->) і закінчується п'ятницею
        if current_date.weekday() in (5, 6):
            iterator.append(current_date)
        elif iterator:
            iterator.append(current_date)
        current_date += timedelta(days=1)

    output = {}  # Словник, який буде зберігати імена іменинників, ключі якого це дні тижня. Завчасно ключі не створюємо
    for count, val in enumerate(iterator):  # Ітеруємо по списку днів тижня
        for user in users:  # Ітеруємо по списку словників з даними співробітників
            if val.day == user["birthday"].day and val.month == user["birthday"].month:  # Перевірка на день народження
                if not output.get(b_day_dict[val.weekday()]):  # Якщо ключ дня тижня поки не існує
                    output[b_day_dict[val.weekday()]] = [user["name"]]
                else:  # Якщо під таким ключем вже є дані
                    output[b_day_dict[val.weekday()]].append(user["name"])

    for key, val in output.items():  # Виводимо результат
        print(f'{key}: {", ".join(val)}')


if __name__ == "__main__":
    main()
