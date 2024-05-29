from datetime import datetime, timedelta
from collections import UserDict
import re
from abc import ABC, abstractmethod

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'{self.value}'


class Birthday(Field):
    def __init__(self, value):
        if not self.is_valid_date_format(value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(datetime.strptime(value, "%d.%m.%Y"))

    def is_valid_date_format(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def __repr__(self):
        return f'{self.value.strftime("%d.%m.%Y")}'


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, phone):
        if self.validate(phone):
            super().__init__(phone)
        else:
            raise Exception("Номер телефону не відповідає формату")

    @staticmethod
    def validate(phonenumber):
        return True if re.match(r"^\d{10}$", phonenumber) else False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
        else:
            print(f'Phone {old_phone} is not exist!')

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        return phone if phone in self.phones else None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Імя: {self.name.value}, телефони: {'; '.join(p.value for p in self.phones)}, дата народження: {self.birthday.value.strftime('%d.%m.%Y') if self.birthday is not None else 'Відсутня'}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, search_name):
        for key, value in self.data.items():
            if key == search_name:
                return value

    def update_record(self, record):
        self.data[record.name.value] = record

    def show(self):
        if len(self.data) == 0:
            print('No data exist!')
        for record in self.data.values():
            print(record)

    def delete(self, search_name):
        if search_name in self.data.keys():
            del self.data[search_name]
            print(f'User {search_name} has been deleted!')

    def get_congratulation_date(self, bday: datetime.date):
        days_delta = 0
        if bday.weekday() in [5, 6]:
            days_delta = 2 if bday.weekday() == 5 else 1

        return bday + timedelta(days=days_delta)

    def get_upcoming_birthdays(self, days_threshold):
        today = datetime.today().date()

        upcoming_birthdays = []
        for record in self.data.values():
            try:
                birthday = record.birthday.value.date().replace(year=today.year)

                if 0 <= (birthday - today).days <= days_threshold:
                    upcoming_birthdays.append({
                        'user': record.name.value,
                        'congratulation_date': self.get_congratulation_date(birthday)
                    })

            except ValueError:
                print(f'Некоректна дата народження для користувача {record.name.value}')

        return upcoming_birthdays


class UserInterface(ABC):
    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_commands_info(self):
        pass



