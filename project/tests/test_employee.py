import unittest

from lib import Employee
from lib import Task


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("GeekMan", 17)

    def test_is_ready_task(self):
        self.assertTrue(self.employee.is_ready_get_task(12))

    def test_add_task(self):
        self.assertEqual(len(self.employee.list_task_getter), 0)
        self.employee.add_task(Task("Task#1", 13))
        self.assertEqual(len(self.employee.list_task_getter), 1)

    def test_total_pointer(self):
        self.assertEqual(self.employee.total_point_getter, 0)
        self.employee.add_task(Task("Task#1", 13))
        self.assertEqual(self.employee.total_point_getter, 13)

if __name__ == '__main__':
    unittest.main()