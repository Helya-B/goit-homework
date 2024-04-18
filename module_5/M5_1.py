def caching_fibonacci():
    cache = {}

    def fibonacci(number):
        # Якщо число в кеші повертаємо значення
        if number in cache:
            return cache[number]

        # Вираховуємо n-е число Фібоначчі
        if number <= 1:
            return number
        else:
            cache[number] = fibonacci(number - 1) + fibonacci(number - 2)

        # Зберігаємо число
        return cache[number]

    return fibonacci


# Приклад:
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(10))  # 55
print(fib(15))  # 610
