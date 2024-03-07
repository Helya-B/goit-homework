import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]


def normalize_phone(number):
    pattern = r"[^\d]"
    replacement = ""

    replaced = re.sub(pattern, replacement, number)
    # result = re.sub(r"^(0)|(38)", "+380", replaced)

    if replaced.startswith("0"):
        prefix = "+38"
    elif replaced.startswith("38"):
        prefix = "+"
    else:
        prefix = ""

    return prefix + replaced


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
