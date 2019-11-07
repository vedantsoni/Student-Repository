import unittest
import HW10_Vedant_Soni

class UnitTests(unittest.TestCase):
    """ Unit test case class that incorporates test cases for both student and instructor's function """
    
    vdir = 'C:/Users/VedantS/Desktop/files'
    uni = HW10_Vedant_Soni.Repository(vdir, False)

    def test_university_student(self):
        """ Unit Test case to test the student function """

        pt_students = [["10103", "Baldwin, C", "SFEN", ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, None],
            ["10115", "Wyatt, X", "SFEN", ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, None],
            ["10172", "Forbes, I", "SFEN", ['SSW 555', 'SSW 567'], {'SSW 564', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}],
            ["10175", "Erickson, D", "SFEN", ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}],
            ["10183", "Chapman, O", "SFEN", ['SSW 689'], {'SSW 567', 'SSW 555', 'SSW 564', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}],
            ["11399", "Cordova, I", "SYEN", ['SSW 540'], {'SYS 612', 'SYS 800', 'SYS 671'}, None],
            ["11461", "Wright, U", "SYEN", ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
            ["11658", "Kelly, P", "SYEN", [], {'SYS 800', 'SYS 612', 'SYS 671'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
            ["11714", "Morton, A", "SYEN", ['SYS 611', 'SYS 645'], {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
            ["11788", "Fuller, E", "SYEN", ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None]]

        students = [val.pt_row() for val in UnitTests.uni._students.values()]
        self.assertEqual(students, pt_students)

    def test_university_instructor(self):
        """ Unit Test case to test the instructor function """
        
        pt_instructors = [
            ['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
            ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
            ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
            ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
            ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
            ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
            ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
            ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1],
        ]

        instructors = [row for instructor in UnitTests.uni._instructors.values() for row in instructor.pt_row()]
        self.assertEqual(instructors, pt_instructors)

    def test_university_majors(self):
        """ Unit Test case to test the majors function """

        pt_majors = [
            ["SFEN", {'SSW 555', 'SSW 567', 'SSW 564', 'SSW 540'}, {'CS 513', 'CS 501', 'CS 545'}], 
            ["SYEN", {'SYS 671', 'SYS 800', 'SYS 612'}, {'SSW 565', 'SSW 810', 'SSW 540'}]
        ]

        majors = [m.pt_row() for m in UnitTests.uni._majors.values()]
        self.assertEqual(majors, pt_majors)
    
unittest.main(exit=False, verbosity=2)

