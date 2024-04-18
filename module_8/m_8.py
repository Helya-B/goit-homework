from address_book import AddressBook, Record
from colorama import Fore
import pickle


def errors_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print(f"{Fore.RED} [Error] {Fore.RESET} Будь ласка, введіть команду")
        except KeyError:
            print(f"{Fore.RED} [Error] {Fore.RESET} Будь ласка, введіть команду")
        except ValueError:
            print(
                f"{Fore.RED} [Error] {Fore.RESET} Параметри введено не коректно. Для прикладу 'add Olena 0932223355 ")

    return wrapper


@errors_handler
def parse_input(user_input):
    tokens = user_input.lower().split()
    command = tokens[0]
    args = tokens[1:]
    return command, args


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def init_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():

    print("Вітаю, Ваш асистент готовий до роботи!!\n")
    print("Доступні команди:")

    commands = [
        "add <і`мя> <номер>",
        "phone <і`мя>",
        "change <і`мя> <cтарий номер> <новий номер>",
        "all",
        "add-birthday <ім`я> <дата>",
        "show-birthday <ім`я>",
        "birthdays",
        "hello",
        "exit"
    ]

    for command in commands:
        print(f"\t{command}")

    book = init_data()

    while True:
        user_input = input("\nВведіть команду: ")
        command, args = parse_input(user_input)

        if command == "add":
            if len(args) != 2:
                print("Невірний формат команди. Використайте: add <і`мя> <номер>")
            else:
                record = Record(args[0])
                try:
                    record.add_phone(args[1])
                    book.add_record(record)
                    print(f"Контакт {args[0]} з номером {args[1]} доданий до книги.")
                except Exception as e:
                    print(e)

        elif command == "phone":
            if len(args) != 1:
                print("Невірний формат команди. Використайте: phone <і`мя>")
            else:
                record = book.find(args[0])
                if record is None:
                    print(f"Контакт {args[0]} не знайдено")
                else:
                    print(f"Телефони для {args[0]}: {', '.join(record.phones)}")

        elif command == "change":
            if len(args) != 3:
                print("Невірний формат команди. Використайте: change <і`мя> <cтарий номер> <новий номер>")
            else:
                record = book.find(args[0])
                if record is None:
                    print(f"Контакт {args[0]} не знайдено")
                record.edit_phone(args[1], args[2])
                book.update_record(record)
                print(f"Телефон {args[1]} для {args[0]} змінено на {args[2]}")
        elif command == "all":
            book.show()
        elif command == "add-birthday":
            if len(args) != 2:
                print("Невірний формат команди. Використайте: add-birthday <ім`я> <дата>")
            else:
                record = book.find(args[0])
                if record is None:
                    print(f"Контакт {args[0]} не знайдено")
                else:
                    record.add_birthday(args[1])
                    book.update_record(record)
                    print(f"Додано день народження для {args[0]}")
        elif command == "show-birthday":
            if len(args) != 1:
                print("Невірний формат команди. Використайте: show-birthday <ім`я>")
            else:
                record = book.find(args[0])
                if record is None:
                    print(f"Контакт {args[0]} не знайдено")
                print(record.birthday.value.date())

        elif command == "birthdays":
            print("Ближчі дні народження:")
            for birthday in book.get_upcoming_birthdays(7):
                print(f"{birthday['user']} - {birthday['congratulation_date']}")

        elif command == "exit" or command == "close":
            try:
                save_data(book)
            except Exception as e:
                print(f"Помилка збереження даних: {e}")
            print("Программа завершена.")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Невідома команда. Спробуйте знову.")


if __name__ == "__main__":
    main()
