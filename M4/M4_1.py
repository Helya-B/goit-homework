def total_salary(path):
    sum_salary = 0
    num_employees = 0
    try:

        with open(path, 'r') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = float(salary_str)
                sum_salary += salary
                num_employees += 1

        if num_employees == 0:
            return 0, 0

        return sum_salary / num_employees, sum_salary

    except FileNotFoundError:
        print(f'Вибачте, але файл {path} відсутній')


file_path = 'Data/salaries.txt'
average_salary, total_salary = total_salary(file_path)
print("Середня зарплата співробітників:", average_salary)
print("Сума усіх зарплат:", total_salary)
