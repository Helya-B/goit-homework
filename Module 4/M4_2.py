def get_cats_info(path):
    cats_info = []
    with open(path, 'r', encoding='UTF8') as file:
        for line in file:
            id, name, age = line.strip().split(',')
            entry = {
                'id': id.strip(),
                'name': name.strip(),
                'age': age.strip()
            }
            cats_info.append(entry)

    return cats_info


path = 'Data/cats.txt'
try:
    parsed_сats_info = get_cats_info(path)
    print(parsed_сats_info)
except FileNotFoundError:
    print(f'Вибачте, але файл {path} відсутній')
except ValueError:
    print(f'Дані не повні')
