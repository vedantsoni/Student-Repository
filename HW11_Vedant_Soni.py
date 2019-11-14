from collections import defaultdict
from prettytable import PrettyTable
from HW08_Vedant_Soni import file_reading_gen
import os
import sqlite3

class Major:
    """ Class that incorporates major functions """

    pt_labels = ['Dept', 'Required', 'Electives']

    def __init__(self, name, passing=None):
        self._name = name
        self._required = set()
        self._electives = set()

        if passing is None:
            self.passing_grades = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def add_course(self, flag, course):
        if flag == 'E':
            self._electives.add(course)
        elif flag == 'R':
            self._required.add(course)
        else:
            raise ValueError('No Courses found')

    def grade_check(self, courses):
        complete_course = {course for course, grade in courses.items() if grade in self.passing_grades}
        if complete_course == '{}':
            return[complete_course, self._required, self._electives]
        else:
            remaining_required = self._required - complete_course
            if self._electives.intersection(complete_course):
                remaining_electives = None
            else:
                remaining_electives = self._electives

            return [complete_course, remaining_required, remaining_electives]

    def pt_row(self):
        return [self._name, self._required, self._electives]


class Student:
    """ Class that incorporates student functions """

    pt_labels = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives']

    def __init__(self, cwid, name, major, name_major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._name_major = name_major

        self._courses = dict()

    def add_course(self, course, grade):
        grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
        if grade in grades:
            self._courses[course] = grade

    def pt_row(self):
        completed_courses, rem_required, rem_electives = self._name_major.grade_check(self._courses)
        return [self._cwid, self._name, self._major, sorted(completed_courses), rem_required, rem_electives]


class Instructor:
    """ Class that incorporates Instructor functions """

    pt_labels = ['CWID', 'Name', 'Department', 'Course', 'Students']

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
    """ Class that incorporates Repository functions """
    
    def __init__(self, vdir, ptables=True):
        self._vdir = vdir
        self._students = dict()
        self._instructors = dict()
        self._majors = dict()
        self.read_instructors(os.path.join(vdir, 'instructors.txt'))
        self.read_majors(os.path.join(vdir, 'majors.txt'))
        self.read_students(os.path.join(vdir, 'students.txt'))
        self.read_grades(os.path.join(vdir, 'grades.txt'))

        if ptables:
            print("\n Major Summary")
            self.major_prettytable()

            print("\n Student's Summary")
            self.student_prettytable()

            # print("\n Instructor's Summary")
            # self.instructor_prettytable()

            print("\n Instructor's Summary")
            self.instructor_table_db('C:/Users/VedantS/Desktop/SQLLite/810_startup.db')


    def read_students(self, path):
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep='\t', header=True):
                if cwid in self._students:
                    raise ValueError('CWID already exists')
                else:
                    self._students[cwid] = Student(cwid, name, major, self._majors[major])

        except ValueError as e:
            raise ValueError(e)

    def read_instructors(self, path):
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep ='\t', header=True):
                if cwid in self._instructors:
                    raise ValueError('CWID already exists')
                else:
                    self._instructors[cwid] = Instructor(cwid, name, dept)

        except ValueError as e:
            raise ValueError(e)

    def read_grades(self, path):
        try:
            for student_cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep='\t', header=True):
                if student_cwid in self._students:
                    self._students[student_cwid].add_course(course, grade)
                else:
                    raise ValueError("Students CWID cannot be found")

                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].add_course(course)
                else:
                    raise ValueError("Instructors CWID cannot be found")

        except ValueError as e:
            raise ValueError(e)

    def read_majors(self, path):
        try:
            for major, flag, course in file_reading_gen(path, 3, sep='\t', header=True):
                if major in self._majors:
                    self._majors[major].add_course(flag, course)
                else:
                    self._majors[major] = Major(major)
                    self._majors[major].add_course(flag, course)

        except:
            ValueError('No majors found')

    def major_prettytable(self):
        pt = PrettyTable(field_names = Major.pt_labels)
        for major in self._majors.values():
            pt.add_row(major.pt_row())

        print(pt)

    def student_prettytable(self):
        pt = PrettyTable(field_names = Student.pt_labels)
        for student in self._students.values():
            pt.add_row(student.pt_row())

        print(pt)

    # def instructor_prettytable(self):
    #     pt = PrettyTable(field_names = Instructor.pt_labels)
    #     for instructor in self._instructors.values():
    #         for row in instructor.pt_row():
    #             pt.add_row(row)

    #     print(pt)

    def  instructor_table_db(self, db_path):
    
        pt = PrettyTable(field_names = Instructor.pt_labels)
        db_path =  'C:/Users/VedantS/Desktop/SQLLite/810_startup.db'
        db = sqlite3.connect(db_path)
        query = """select instructors.CWID, instructors.Name, instructors.Dept, grades.Course, count(*) as Students from instructors natural join grades where instructors.CWID = grades.InstructorCWID group by instructors.CWID, grades.Course order by Students desc; """
        for row in db.execute(query):
            pt.add_row(row)
        
        print(pt)


def main():
    Repository('C:/Users/VedantS/Desktop/Text Files')

if __name__ == '__main__':
    main()