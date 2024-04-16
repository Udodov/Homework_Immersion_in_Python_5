"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""

from typing import List


def calculate_bonus(names: List[str], rates: List[int], bonuses: List[str]) -> dict:
    return {name: rate * float(bonus.rstrip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}


# Пример использования
names_input = ["Сергей", "Иван", "Ольга"]
rates_input = [1000, 1500, 1200]
bonuses_input = ["10%", "15.5%", "12%"]

bonus_dict = calculate_bonus(names_input, rates_input, bonuses_input)
print(bonus_dict)
