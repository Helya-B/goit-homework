from datetime import datetime

date = '2024.02.15'


def get_days_from_today(date):
    date_datetime = datetime.strptime(date, "%Y.%m.%d")
    date_now = datetime.today()
    diff = date_now - date_datetime
    return diff.days


print(get_days_from_today(date))
