import os
from pathlib import Path

file_types = ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff']


def sort_elem(path_dir):
    cur_dir = Path(path_dir)
    for object in cur_dir.iterdir():
        if object.is_dir() and not os.listdir(object.absolute()):
            object.rmdir()
            print(f'Removed empty folder {object.name}')

        file_suffix = object.suffix.lower().replace('.', '')
        if file_suffix in file_types:
            new_path = cur_dir / file_suffix
            new_path.mkdir(exist_ok=True)
            object.rename(new_path.joinpath(object.name))


path_d = input('[+] Введіть шлях сортування: ')
if not Path(path_d).exists():
    print('[-] Директорія відсутня')
else:
    sort_elem(path_d)
print('[!] Сортування завершено')
