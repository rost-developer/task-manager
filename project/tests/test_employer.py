import unittest

from lib import Employer


class TestCmdParameters(unittest.TestCase):

    def test_is_ready_task(self):
        employer = Employer("GeekMan", 17)
        self.assertTrue(employer.is_ready_get_task(12))

if __name__ == '__main__':
    unittest.main()