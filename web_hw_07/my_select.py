
from sqlalchemy import (
    func,
    desc,
    and_,)
from sqlalchemy import select
from connect_db import session
from models import Teacher, Student, Group, Discipline, Grade


def select_1():

    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


def select_2(discipline_id: int):

    result = (
        session.query(
            Discipline.name,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return result


def select_3(discipline_id: int):

    result = (
        session.query(
            Group.fullname,
            Discipline.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Group.fullname, Discipline.name)
        .order_by("avg_grade")
        .all()
    )
    return result


def select_4():

    result = (
        session.query(func.round(func.avg(Grade.grade), 2)).select_from(Grade).all()
    )
    return result


def select_5(teacher_id: int):

    result = (
        session.query(Teacher.fullname, Discipline.name)
        .select_from(Teacher)
        .join(Discipline)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.fullname, Discipline.name)
        .order_by(Discipline.name)
        .all()
    )
    return result


def select_6(group_id: int):

    result = (
        session.query(Group.fullname, Student.fullname)
        .select_from(Group)
        .join(Student)
        .filter(Group.id == group_id)
        .group_by(Group.fullname, Student.fullname)
        .order_by(Student.fullname)
        .all()
    )
    return result


def select_7(group_id: int, discipline_id: int):

    result = (
        session.query(Group.fullname, Discipline.name, Grade.grade)
        .select_from(Group)
        .join(Student)
        .join(Grade)
        .join(Discipline)
        .filter(Group.id == group_id)
        .filter(Discipline.id == discipline_id)
        .group_by(Group.fullname, Discipline.name, Grade.grade)
        .all()
    )
    return result


def select_8(teacher_id: int):

    result = (
        session.query(
            Teacher.fullname,
            Discipline.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Discipline)
        .join(Teacher)
        .join(Grade)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.fullname, Discipline.name)
        .order_by("avg_grade")
        .all()
    )
    return result


def select_9(student_id: int):

    result = (
        session.query(Student.fullname, Discipline.name)
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Student.id == student_id)
        .group_by(Student.fullname, Discipline.name)
        .order_by(Student.fullname)
        .all()
    )
    return result


def select_10(student_id: int, teacher_id: int):

    result = (
        session.query(Student.fullname, Teacher.fullname, Discipline.name)
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .filter(Student.id == student_id)
        .group_by(Student.fullname, Teacher.fullname, Discipline.name)
        .order_by(Discipline.name)
        .all()
    )
    return result


def select_11(student_id: int, teacher_id: int):

    result = (
        session.query(
            Teacher.fullname,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Student)
        .join(Grade)
        .join(Discipline)
        .join(Teacher)
        .filter(Student.id == student_id)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.fullname, Student.fullname)
        .all()
    )
    return result


def select_12(discipline_id: int, group_id: int):

    subquery = (
        select(Grade.date_of)
        .join(Student)
        .join(Group)
        .where(and_(Grade.discipline_id == discipline_id, Group.id == group_id))
        .order_by(desc(Grade.date_of))
        .limit(1)
        .scalar_subquery()
    )

    result = (
        session.query(
            Discipline.name,
            Student.fullname,
            Group.fullname,
            Grade.date_of,
            Grade.grade,
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(
            and_(
                Discipline.id == discipline_id,
                Group.id == group_id,
                Grade.date_of == subquery,
            )
        )
        .order_by(desc(Grade.date_of))
        .all()
    )
    return result


if __name__ == "__main__":
    # print(select_1())
    # print(select_2(1))
    # print(select_3(2))
    # print(select_4())
    # print(select_5(1))
    # print(select_6(2))
    # print(select_7(1, 5))
    # print(select_8(2))
    # print(select_9(4))
    # print(select_10(5, 2))
    # print(select_11(5, 1))
    print(select_12(5, 1))