import unittest

from lib import State
from lib import Employer


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.employer = Employer("Cudo", 34)

    def test_add_employer(self):
        self.assertEqual(len(self.state.state_getter), 0)
        self.state.add_employer(self.employer)
        self.assertEqual(len(self.state.state_getter), 1)

    def test_exists_employer(self):
        self.state.add_employer(self.employer)
        self.assertTrue(self.state.search_employer("Cudo"))

    def test_search_employer(self):
        self.state.add_employer(self.employer)
        self.assertEqual(self.state.search_employer("Cudo"), self.employer)

    def test_search_employer_false(self):
        self.state.add_employer(self.employer)
        self.assertFalse(self.state.search_employer("Robert"))

    if __name__ == '__main__':
        unittest.main()
