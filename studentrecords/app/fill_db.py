# -*- coding: utf-8 -*-

import datetime
from models.user_profile import UserProfile
from models.attendance import Attendance, AttendanceRecord
from models.grades import Grades, Lesson, Lab
from models.term_project import TermProject, Project


def add_users():
    UserProfile.create(login='admin',
                       password='123',
                       email='admin@gmail.com',
                       first_name='fname',
                       last_name='lname',
                       type='a',
                       is_superuser=True)

    UserProfile.create(login='teacher',
                       password='123',
                       email='teacher@gmail.com',
                       first_name='fname',
                       last_name='lname',
                       type='t')

    UserProfile.create(login='head',
                       password='123',
                       email='head@gmail.com',
                       first_name='fname',
                       last_name='lname',
                       type='h')

    for i in range(3):
        student = ('student%s' % i)
        UserProfile.create(login=student,
                           password='123',
                           email=('%s@gmail.com' % student),
                           first_name=('%s_fn' % student),
                           last_name=('%s_ln' % student),
                           study_group='2304',
                           type='s')


def add_attendance():
    student0 = UserProfile.objects.get_by_login(login='student0').id
    student1 = UserProfile.objects.get_by_login(login='student1').id
    student2 = UserProfile.objects.get_by_login(login='student2').id

    Attendance.create(student_id=student0,
                      attendance_records=[
                          AttendanceRecord(lesson_name='Информатика', date=datetime.date.today()),
                          AttendanceRecord(lesson_name='Программирование', date=datetime.date.today())
                      ])

    Attendance.create(student_id=student1,
                      attendance_records=[
                          AttendanceRecord(lesson_name='Информатика', date=datetime.date.today()),
                          AttendanceRecord(lesson_name='Программирование', date=datetime.date.today())
                      ])

    Attendance.create(student_id=student2,
                      attendance_records=[
                          AttendanceRecord(lesson_name='Информатика', date=datetime.date.today()),
                          AttendanceRecord(lesson_name='Программирование', date=datetime.date.today())
                      ])


def add_grades():
    student0 = UserProfile.objects.get_by_login(login='student0').id
    student1 = UserProfile.objects.get_by_login(login='student1').id
    student2 = UserProfile.objects.get_by_login(login='student2').id

    Grades.create(student_id=student0,
                  grades=[
                      Lesson(name='Информатика', labs=[
                          Lab(title='Лаба1', grade=3.0),
                          Lab(title='Лаба2', grade=4.0),
                          Lab(title='Лаба3', grade=5.0)
                      ]),

                      Lesson(name='Программирование', labs=[
                          Lab(title='Лаба1', grade=5.0),
                          Lab(title='Лаба2', grade=4.0),
                          Lab(title='Лаба3', grade=3.0)
                      ])
                  ])

    Grades.create(student_id=student1,
                  grades=[
                      Lesson(name='Информатика', labs=[
                          Lab(title='Лаба1', grade=3.0),
                          Lab(title='Лаба2', grade=4.0),
                          Lab(title='Лаба3', grade=5.0)
                      ]),

                      Lesson(name='Программирование', labs=[
                          Lab(title='Лаба1', grade=5.0),
                          Lab(title='Лаба2', grade=4.0),
                          Lab(title='Лаба3', grade=3.0)
                      ])
                  ])

    Grades.create(student_id=student2,
                  grades=[
                      Lesson(name='Информатика', labs=[
                          Lab(title='Лаба1', grade=3.0),
                          Lab(title='Лаба2', grade=4.0),
                          Lab(title='Лаба3', grade=5.0)
                      ]),

                      Lesson(name='Программирование', labs=[
                          Lab(title='Лаба1', grade=5.0),
                          Lab(title='Лаба2', grade=4.0),
                          Lab(title='Лаба3', grade=3.0)
                      ])
                  ])


def add_term_projects():
    student0 = UserProfile.objects.get_by_login(login='student0').id
    student1 = UserProfile.objects.get_by_login(login='student1').id
    student2 = UserProfile.objects.get_by_login(login='student2').id

    TermProject.create(student_id=student0,
                       projects=[
                           Project(lesson_name='Информатика',
                                   project_title='Title1',
                                   github_link='link1'),

                           Project(lesson_name='Программирование',
                                   project_title='Title2',
                                   github_link='link2')
                       ])

    TermProject.create(student_id=student1,
                       projects=[
                           Project(lesson_name='Информатика',
                                   project_title='Title1',
                                   github_link='link1'),

                           Project(lesson_name='Программирование',
                                   project_title='Title2',
                                   github_link='link2')
                       ])

    TermProject.create(student_id=student2,
                       projects=[
                           Project(lesson_name='Информатика',
                                   project_title='Title1',
                                   github_link='link1'),

                           Project(lesson_name='Программирование',
                                   project_title='Title2',
                                   github_link='link2')
                       ])


def main():
    add_users()
    add_grades()
    add_attendance()
    add_term_projects()


if __name__ == '__main__':
    main()
