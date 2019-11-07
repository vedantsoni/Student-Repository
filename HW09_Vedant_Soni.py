from collections import defaultdict
from prettytable import PrettyTable
from HW08_Vedant_Soni import file_reading_gen
import unittest
import os

os.chdir('C:/Users/VedantS/Desktop/files')


class Student:
    """ Class that incorporates student functions """

    pt_labels = ['CWID', 'Name', 'Completed Courses']

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._courses = dict()

    def add_course(self, course, grade):
        self._courses[course] = grade

    def pt_row(self):
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """ Class that incorporates Instructor functions """

    pt_labels = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)

    def add_course(self, course):
        self._courses[course] += 1

    def pt_row(self):
        for course, students in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, students]


class Repository:
    """ Class that incorporates repository functions """

    def __init__(self, vdir, ptables=True):
        self._vdir = vdir
        self._students = dict()
        self._instructors = dict()
        self.read_students(os.path.join(vdir, 'students.txt'))
        self.read_instructors(os.path.join(vdir, 'instructors.txt'))
        self.read_grades(os.path.join(vdir, 'grades.txt'))

        if ptables:
            print("\n Student's Summary")
            self.student_prettytable()

            print("\n Instructor's Summary")
            self.instructor_prettytable()

    def read_students(self, path):
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep = '\t', header=False):
                if cwid in self._students:
                    raise Exception
                else:
                    self._students[cwid] = Student(cwid, name, major)

        except ValueError as e:
            raise ValueError(e)

    def read_instructors(self, path):
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep = '\t', header=False):
                if cwid in self._instructors:
                    raise Exception
                else:
                    self._instructors[cwid] = Instructor(cwid, name, dept)

        except ValueError as e:
            raise ValueError(e)

    def read_grades(self, path):
        try:
            for student_cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep ='\t', header=False):
                if student_cwid in self._students:
                    self._students[student_cwid].add_course(course, grade)
                else:
                    raise NameError

                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].add_course(course)
                else:
                    raise NameError

        except ValueError as e:
            raise ValueError(e)

    def student_prettytable(self):
        pt = PrettyTable(field_names = Student.pt_labels)
        for student in self._students.values():
            pt.add_row(student.pt_row())

        print(pt)

    def instructor_prettytable(self):
        pt = PrettyTable(field_names = Instructor.pt_labels)
        for instructor in self._instructors.values():
            for row in instructor.pt_row():
                pt.add_row(row)

        print(pt)
        

def main():
    Repository('C:/Users/VedantS/Desktop/files')

if __name__ == '__main__':
    main()