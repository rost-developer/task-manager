import unittest

from lib import State
from lib import Employee


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.employee = Employee("Cudo", 34)

    def test_add_employee(self):
        self.assertEqual(len(self.state.state_getter), 0)
        self.state.add_employee(self.employee)
        self.assertEqual(len(self.state.state_getter), 1)

    def test_exists_employee(self):
        self.state.add_employee(self.employee)
        self.assertTrue(self.state.search_employee("Cudo"))

    def test_search_employee(self):
        self.state.add_employee(self.employee)
        self.assertEqual(self.state.search_employee("Cudo"), self.employee)

    def test_search_employee_false(self):
        self.state.add_employee(self.employee)
        self.assertFalse(self.state.search_employee("Robert"))

    if __name__ == '__main__':
        unittest.main()
