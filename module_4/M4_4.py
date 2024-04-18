def parse_input(user_input):
    tokens = user_input.lower().split()
    command = tokens[0]
    args = tokens[1:]
    return command, args


def add_contact(phonebook, name, phone_number): # Додавання контактів
    if name in phonebook:
        print("Koнтакт вже існує")
        return

    phonebook[name] = phone_number

    with open("Data/phonebook.txt", "a") as file: # Зберігання контактів
        file.write(f"{name} {phone_number}\n")

    print(f"Контакт {name} з номером {phone_number}  додали до книги.")


def delete_contact(phonebook, name_to_delete): # ВИдалення контакта по імені
        if name_to_delete in phonebook:
            del phonebook[name_to_delete]
            print(f"Контакт {name_to_delete} видалено.")
        else:
            print(f"Контакт {name_to_delete} не знайден.")

        with open("Data/phonebook.txt", "r") as file:
            lines = file.readlines()
        with open("Data/phonebook.txt", "w") as file:
            for line in lines:
                if not line.startswith(name_to_delete):
                    file.write(line)


def update_contact(phonebook, name, new_phone_number): # Зміна контакту
    if name in phonebook:
        delete_contact(phonebook, name)
        add_contact(phonebook, name, new_phone_number)
        print(f"Контакт {name} оновлений з новим номером {new_phone_number}.")
    else:
        print(f"Контакт {name} не знайдено.")


def show_phone(phonebook, name): # Пошук номера по імені
    if name in phonebook:
        print(f"Номер телефона для {name}: {phonebook[name]}")
    else:
        print(f"Контакт {name} не знайдено.")


def main():
    print("Вітаю, Ваш асистент готовий до роботи!!")
    phonebook = {}  # Словник телефонів

    with open("Data/phonebook.txt", "r") as file:
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
