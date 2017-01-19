import unittest

from lib import Employer
from lib import Task


class TestEmployer(unittest.TestCase):

    def setUp(self):
        self.employer = Employer("GeekMan", 17)

    def test_is_ready_task(self):
        self.assertTrue(self.employer.is_ready_get_task(12))

    def test_add_task(self):
        self.assertEqual(len(self.employer.list_task_getter), 0)
        self.employer.add_task(Task("Task#1", 13))
        self.assertEqual(len(self.employer.list_task_getter), 1)

    def test_total_pointer(self):
        self.assertEqual(self.employer.total_point_getter, 0)
        self.employer.add_task(Task("Task#1", 13))
        self.assertEqual(self.employer.total_point_getter, 13)

if __name__ == '__main__':
    unittest.main()