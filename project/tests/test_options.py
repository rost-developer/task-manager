import unittest

from lib import Options


class TestCmdParameters(unittest.TestCase):
    def setUp(self):
        self.options = Options()

    def test_defaults_options_are_set(self):
        opts = self.options.parse([])
        self.assertEquals(opts.numb_person, 10)
        self.assertEquals(opts.numb_tasks, 30)

    def test_options_numb_person_is_set(self):
        opts = self.options.parse(['-p', '40'])
        self.assertEquals(opts.numb_person, 40)

        opts = self.options.parse(['--numb_person', '50'])
        self.assertEquals(opts.numb_person, 50)

    def test_options_numb_tasks_is_set(self):
        opts = self.options.parse(['-t', '400'])
        self.assertEquals(opts.numb_tasks, 400)

        opts = self.options.parse(['--numb_tasks', '500'])
        self.assertEquals(opts.numb_tasks, 500)


if __name__ == '__main__':
    unittest.main()
