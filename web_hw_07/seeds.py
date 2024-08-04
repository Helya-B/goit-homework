from connect_db import session
from models import Teacher, Student, Group, Discipline, Grade
from faker import Faker

if __name__ == '__main__':
    fake = Faker()

    groups = [('Group 1',), ('Group 2',), ('Group 3',)]

    for group in groups:
        session.add(Group(fullname=group[0]))

    for teacher in [(fake.name(),) for _ in range(5)]:
        session.add(Teacher(fullname=teacher[0]))

    for discipline in [(fake.word(),) for _ in range(5)]:
        session.add(Discipline(name=discipline[0], teacher_id=fake.random_int(1, 5)))

    for student in [(fake.name(),) for _ in range(40)]:
        session.add(Student(fullname=student[0], group_id=fake.random_int(1, 3)))

    for student_id in range(1, 41):
        for grade in [(fake.random_int(1, 5), fake.date_time_this_year()) for _ in range(20)]:
            session.add(
                Grade(grade=grade[0], date_of=grade[1], student_id=student_id, discipline_id=fake.random_int(1, 5)))
    session.commit()
