from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'{self.value}'


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, phone):
        if self.validate(phone):
            super().__init__(phone)
        else:
            raise Exception("Phone number is not valid")

    @staticmethod
    def validate(phonenumber):
        return True if re.match(r"^\d{10}$", phonenumber) else False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                print(f'Phone {old_phone} edited to {new_phone}')
                break
        else:
            print(f'Phone {old_phone} is not exist!')

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        return phone if phone in self.phones else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    current_id = 1

    def add_record(self, record):
        self.data[AddressBook.current_id] = record
        AddressBook.current_id += 1

    def find(self, search_name):
        for key, value in self.data.items():
            if value.name.value == search_name:
                return value

    def show(self):
        if len(self.data) == 0:
            print('No data exist!')
        for record in self.data.values():
            print(record)

    def delete(self, search_name):
        found_key = None
        for key, value in self.data.items():
            if value.name.value == search_name:
                found_key = key
        if found_key:
            del self.data[found_key]
            print(f'User {search_name} has been deleted!')
    ############################################


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
