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


if __name__ == '__main__':
    unittest.main()
