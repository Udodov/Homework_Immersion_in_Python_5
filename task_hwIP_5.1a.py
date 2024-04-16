"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла. (с использованием библиотеки pathlib)"""

from pathlib import Path
from typing import Tuple


def parse_file_path(path: str) -> Tuple[str, str, str]:
    path_obj = Path(path)
    return str(path_obj.parent), path_obj.stem, path_obj.suffix


# Пример использования
file_path = "/home/user/documents/report.txt"
parsed_path = parse_file_path(file_path)
print(parsed_path)
