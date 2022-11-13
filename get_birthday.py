from datetime import datetime, timedelta
import calendar


def main():
    """
    Ця функція існує лише для тестування програми. Викликає функцію 'get_birthdays_per_week()',
    підставляючи в неї список словників.
    """

    users = [{"name": "Aaron", "birthday": datetime(year=1995, month=1, day=1)},
             {"name": "Billy", "birthday": datetime(year=2000, month=1, day=3)},
             {"name": "Cass", "birthday": datetime(year=1995, month=12, day=31)},
             {"name": "Derek", "birthday": datetime(year=2000, month=12, day=30)},
             {"name": "Eugine", "birthday": datetime(year=1995, month=1, day=4)},
             {"name": "Frank", "birthday": datetime(year=2000, month=12, day=28)},
             {"name": "George", "birthday": datetime(year=1995, month=7, day=21)},
             {"name": "Howard", "birthday": datetime(year=2000, month=12, day=30)},
             {"name": "Ian", "birthday": datetime(year=1995, month=9, day=25)},
             {"name": "James", "birthday": datetime(year=2000, month=10, day=23)},
             {"name": "Karen", "birthday": datetime(year=1995, month=11, day=19)},
             {"name": "Larry", "birthday": datetime(year=2000, month=12, day=14)},
             {"name": "Monika", "birthday": datetime(year=1995, month=11, day=23)},
             {"name": "Nigel", "birthday": datetime(year=2000, month=11, day=16)},
             {"name": "Olivia", "birthday": datetime(year=1995, month=11, day=20)},
             {"name": "Peter", "birthday": datetime(year=2000, month=11, day=25)},
             {"name": "Quentin", "birthday": datetime(year=1995, month=1, day=1)},
             {"name": "Robert", "birthday": datetime(year=2000, month=2, day=17)},
             {"name": "Sierra", "birthday": datetime(year=1995, month=3, day=3)},
             {"name": "Tyler", "birthday": datetime(year=2000, month=4, day=9)},
             {"name": "Utah", "birthday": datetime(year=1995, month=5, day=5)},
             {"name": "Voldemar", "birthday": datetime(year=2000, month=6, day=7)},
             {"name": "Wottard", "birthday": datetime(year=1995, month=7, day=22)},
             {"name": "Xarxes", "birthday": datetime(year=2000, month=8, day=11)},
             {"name": "Yulia", "birthday": datetime(year=1995, month=9, day=30)},
             {"name": "Zacharius", "birthday": datetime(year=2000, month=11, day=25)}]

    get_birthdays_per_week(users)


def get_birthdays_per_week(users):
    """
    Функція приймає список словників із даними співробітників.
    Виводить на екран список людей, яких необхідно привітати з днем народження наступного тижня. Враховує
    дні народження на вихідних поточного тижня, записуючи їх на понеділок.
    """
    if not users:  # Перевіряє чи був наданий аргумент
        print("No input was given.")
    current_date = datetime.today()
    print(f"Current day: {calendar.day_name[current_date.weekday()]}\nListing the birthdays for the upcoming week:")
    iterator = []  # Зберігаємо об'єкти datetime, які відповідають дням на наступному тижні і двом вихідним цього тижня
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
    for user in users:  # Ітеруємо по списку словників з даними співробітників
        user_b_day = datetime(year=current_date.year, month=user["birthday"].month, day=user["birthday"].day)
        if user_b_day < iterator[0] or user_b_day > iterator[6]:  # Перевірка на день народження
            continue
        if not output.get(user_b_day.strftime("%A")):  # Ключа немає в словнику. Додаємо.
            if user_b_day.weekday() not in (5, 6):
                output[user_b_day.strftime("%A")] = [user["name"]]
            else:
                output["Monday"] = [user["name"]]
        else:  # Ключ вже є в словнику
            if user_b_day.weekday() not in (5, 6):
                output[user_b_day.strftime("%A")].append(user["name"])
            else:
                output["Monday"].append(user["name"])

    for key, val in output.items():  # Виводимо результат
        print(f'{key}: {", ".join(val)}')


if __name__ == "__main__":
    main()
