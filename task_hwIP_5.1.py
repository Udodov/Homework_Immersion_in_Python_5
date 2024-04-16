"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла. (сплитом)"""

import os
from typing import Tuple


def split_file_path(path_to_file: str) -> Tuple[str, str, str]:
    """
    Разделяет путь к файлу на путь к директории, имя файла и расширение файла.

    :param path_to_file: Полный путь к файлу.
    :return: Кортеж, содержащий путь к директории, имя файла и расширение файла.
    """
    # Разделяем путь и имя файла
    path, filename = os.path.split(path_to_file)
    # Разделяем имя файла и расширение
    file_name, file_extension = os.path.splitext(filename)
    # Возвращаем кортеж без избыточных скобок
    return path, file_name, file_extension


# Пример использования функции
example_file_path = "/path/to/your/file.txt"
result = split_file_path(example_file_path)
print(result)  # Выведет: ('/path/to/your', 'file', '.txt')
