"""Создайте функцию генератор чисел Фибоначчи"""

from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1  # Инициализация первых двух чисел последовательности Фибоначчи
    while True:  # Бесконечный цикл для генерации чисел
        yield a  # Возвращаем текущее число Фибоначчи
        a, b = b, a + b  # Обновляем значения для следующих чисел Фибоначчи


# Пример использования генератора
fib_gen = fibonacci()  # Создаем генератор
for _ in range(10):  # Выводим первые 10 чисел Фибоначчи
    print(next(fib_gen))
