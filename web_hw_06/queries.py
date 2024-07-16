import sqlite3


def execute_query(query, params=None):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def query_1():
    with open('query_1.sql', 'r') as file:
        query = file.read()

    results = execute_query(query)
    for row in results:
        print(row)


def query_2(subject_id):
    with open('query_2.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (subject_id,))
    for row in results:
        print(row)


def query_3(subject_id):
    with open('query_3.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (subject_id,))
    for row in results:
        print(row)


def query_4():
    with open('query_4.sql', 'r') as file:
        query = file.read()

    results = execute_query(query)
    for row in results:
        print(row)


def query_5(teacher_id):
    with open('query_5.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (teacher_id,))
    for row in results:
        print(row)


def query_6(group_id):
    with open('query_6.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (group_id,))
    for row in results:
        print(row)


def query_7(group_id, subject_id):
    with open('query_7.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (group_id, subject_id,))
    for row in results:
        print(row)

def query_8(teacher_id):
    with open('query_8.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (teacher_id,))
    for row in results:
        print(row)

def query_9(student_id):
    with open('query_9.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (student_id,))
    for row in results:
        print(row)


def query_10(teacher_id, student_id):
    with open('query_10.sql', 'r') as file:
        query = file.read()

    results = execute_query(query, (teacher_id, student_id))
    for row in results:
        print(row)


if __name__ == "__main__":
    # Приклади виклику функцій запитів
    print("Query 1: Top 5 students with the highest average grades")
    query_1()

    print("\nQuery 2: Student with the highest average grade in a specific subject")
    subject_id = 1  # замініть на необхідний subject_id
    query_2(subject_id)

    print("\nQuery 3: Average grade in groups for a specific subject")
    subject_id = 1  # замініть на необхідний subject_id
    query_3(subject_id)

    print("\nQuery 4: Average grade across all grades")
    query_4()

    print("\nQuery 5: Find what courses a particular teacher teaches.")
    teacher_id = 1  # замініть на необхідний teacher_id
    query_5(teacher_id)

    print("\nQuery 6: Find a list of students in a specific group.")
    group_id = 1  # замініть на необхідний group_id
    query_6(group_id)

    print("\nQuery 7: Find the grades of students in a separate group for a specific subject.")
    group_id = 1  # замініть на необхідний group_id
    subject_id = 1  # замініть на необхідний subject_id
    query_7(group_id, subject_id)

    print("\nQuery 8:Find the average score given by a certain teacher in his subjects.")
    teacher_id = 1  # замініть на необхідний teacher_id
    query_8(teacher_id)

    print("\nQuery 9: Find a list of courses a student is taking.")
    student_id = 1  # замініть на необхідний student_id
    query_9(student_id)

    print("\nQuery 10: Average grade a specific teacher gives to a specific student")
    teacher_id = 1  # замініть на необхідний teacher_id
    student_id = 1  # замініть на необхідний student_id
    query_10(teacher_id, student_id)
