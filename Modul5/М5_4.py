from colorama import Fore

file_path = "phonebook/my_phonebook.txt"


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


@errors_handler
def add_contact(phonebook, name, phone_number):  # Додавання контактів
    if name in phonebook:
        print("Koнтакт вже існує")
        return

    phonebook[name] = phone_number

    with open(file_path, "a") as file:  # Зберігання контактів
        file.write(f"{name} {phone_number}\n")

    print(f"Контакт {name} з номером {phone_number}  додали до книги.")


@errors_handler
def delete_contact(phonebook, name_to_delete):  # ВИдалення контакта по імені
    if name_to_delete in phonebook:
        del phonebook[name_to_delete]
        print(f"Контакт {name_to_delete} видалено.")
    else:
        print(f"Контакт {name_to_delete} не знайден.")

    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if not line.startswith(name_to_delete):
                file.write(line)


@errors_handler
def update_contact(phonebook, name, new_phone_number):  # Зміна контакту
    if name in phonebook:
        delete_contact(phonebook, name)
        add_contact(phonebook, name, new_phone_number)
        print(f"Контакт {name} оновлений з новим номером {new_phone_number}.")
    else:
        print(f"Контакт {name} не знайдено.")


@errors_handler
def show_phone(phonebook, name):  # Пошук номера по імені
    if name in phonebook:
        print(f"Номер телефона для {name}: {phonebook[name]}")
    else:
        print(f"Контакт {name} не знайдено.")


def main():
    print("Вітаю, Ваш асистент готовий до роботи!!")
    phonebook = {}  # Словник телефонів

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, phone = line.strip().split(' ')
            phonebook[name] = phone

    while True:
        user_input = input("Введіть команду (add, show, update, delete, exit): ")
        command, args = parse_input(user_input)

        if command == "add":
            if len(args) != 2:
                print("Невірний формат команди. Використайте: add <і`мя> <номер>")
            else:
                add_contact(phonebook, args[0], args[1])
        elif command == "show":
            if len(args) != 1:
                print("Невірний формат команди. Використайте: show <і`мя>")
            else:
                show_phone(phonebook, args[0])
        elif command == "update":
            if len(args) != 2:
                print("Невірний формат команди. Використайте: add <і`мя> <номер>")
            else:
                update_contact(phonebook, args[0], args[1])
        elif command == "delete" or command == "del":
            if len(args) != 1:
                print("Невірний формат команди. Використайте: delete <ім`я>")
            else:
                delete_contact(phonebook, args[0])
        elif command == "exit" or command == "close":
            print("Программа завершена.")
            break
        else:
            print("Невідома команда. Спробуйте знову.")


if __name__ == "__main__":
    main()
