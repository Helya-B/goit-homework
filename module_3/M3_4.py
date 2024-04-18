from datetime import datetime, timedelta


def get_congratulation_date(bday: datetime.date):
    days_delta = 0
    if bday.weekday() in [5, 6]:
        days_delta = 2 if bday.weekday() == 5 else 1

    return bday + timedelta(days=days_delta)


def get_upcoming_birthdays(users_list, days_threshold):
    today = datetime.today().date()

    upcoming_birthdays = []
    for user in users_list:
        try:
            birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date().replace(year=today.year)

            if 0 <= (birthday - today).days <= days_threshold:
                upcoming_birthdays.append({
                    'user': user['name'],
                    'congratulation_date': get_congratulation_date(birthday)
                })

        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.10"}
]

print(get_upcoming_birthdays(users, 7))
