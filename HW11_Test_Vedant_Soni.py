import unittest
import HW10_Vedant_Soni

class UnitTests(unittest.TestCase):
    """ Unit test case class that incorporates test cases for both student and instructor's function """
    
    vdir = 'C:/Users/VedantS/Desktop/Text Files'
    uni = HW10_Vedant_Soni.Repository(vdir, True)

    def test_university_student(self):
        """ Unit Test case to test the student function """

        pt_students = [
            ['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 540', 'SSW 555'}, None],
            ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 540', 'SSW 555'}, {'CS 546', 'CS 501'}],
            ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 546', 'CS 501'}],
            ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], set(), None]
        ]

        students = [val.pt_row() for val in UnitTests.uni._students.values()]
        self.assertEqual(students, pt_students)

    def test_university_instructor(self):
        """ Unit Test case to test the instructor function """
        
        pt_instructors = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98763', 'Rowland, J', 
                            'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]


        instructors = [row for instructor in UnitTests.uni._instructors.values() for row in instructor.pt_row()]
        self.assertEqual(instructors, pt_instructors)

    def test_university_majors(self):
        """ Unit Test case to test the majors function """

        pt_majors = [
            ['SFEN', {'SSW 810', 'SSW 540', 'SSW 555'}, {'CS 501', 'CS 546'}],
            ['CS', {'CS 570', 'CS 546'}, {'SSW 810', 'SSW 565'}]
        ]

        majors = [m.pt_row() for m in UnitTests.uni._majors.values()]
        self.assertEqual(majors, pt_majors)
    
unittest.main(exit=False, verbosity=2)

