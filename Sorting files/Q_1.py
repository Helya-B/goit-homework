from pathlib import Path
import os

file_mappings = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],
    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],
    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],
    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
    'font': ['otf', 'ttf', 'fon', 'fnt'],
    'gif': ['gif'],
    'exe': ['exe'],
    'bat': ['bat'],
    'apk': ['apk'],
    'lib': ['dll']
}


def sort_elem(path_dir):
    cur_dir = Path(path_dir)
    for file in cur_dir.iterdir():
        if file.is_dir() and not os.listdir(file.absolute()):
            file.rmdir()
            print(f'Removed empty folder {file.name}')

        for fileType in file_mappings:
            if file.suffix.lower().replace('.', '') in file_mappings[fileType]:
                new_path = cur_dir / fileType
                new_path.mkdir(exist_ok=True)
                file.rename(new_path.joinpath(file.name))


path_d = input('[+] Введіть шлях сортування: ')
if not Path(path_d).exists():
    print('[-] Директорія відсутня')
else:
    sort_elem(path_d)
print('[!] Сортування завершено')
input()
