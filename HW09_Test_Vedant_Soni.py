import unittest
import HW09_Vedant_Soni

class UnitTests(unittest.TestCase):
    """ Unit test case class that incorporates test cases for both student and instructor's function """
    
    vdir = 'C:/Users/VedantS/Desktop/files'
    uni = HW09_Vedant_Soni.Repository(vdir, False)

    def test_university_student(self):
        """ Unit Test case to test the student function """

        pt_students = [
            ['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
            ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
            ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
            ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
            ['10183', 'Chapman, O', ['SSW 689']],
            ['11399', 'Cordova, I', ['SSW 540']],
            ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
            ['11658', 'Kelly, P', ['SSW 540']],
            ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
            ['11788', 'Fuller, E', ['SSW 540']]
        ]

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
    
unittest.main(exit=False, verbosity=2)

