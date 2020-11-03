import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Reser', 'Jack', 'CIS', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Reser')
        self.assertEqual(self.student.first_name, 'Jack')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        this_student = s.Student('John', 'Doe', 'CIS', 3.5)
        assert this_student.last_name == 'John'
        assert this_student.first_name == 'Doe'
        assert this_student.major == 'CIS'
        assert this_student.gpa == 3.5

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Reser, Jack has major CIS with gpa: 4.0')



if __name__ == '__main__':
    unittest.main()
