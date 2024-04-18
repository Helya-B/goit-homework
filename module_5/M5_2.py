import re


def generator_numbers(text: str):  # використовуємо рег вирази для пошуку чисел
    pattern = r'\b\d+(\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо найденне число как генератор


def sum_profit(text: str, func):
    # Використовуємо генератор отримання чисел з тексту
    numbers = func(text)
    total_profit = sum(numbers)
    return total_profit


# Пример использования:
text_example = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений "
                "додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text_example, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
