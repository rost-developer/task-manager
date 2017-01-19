import sys
from argparse import ArgumentParser


class Options:
    """
    this class parse parameters command line
    """
    def __init__(self):
        self._init_parse()

    def _init_parse(self):
        usage = 'bin/task_manager.sh'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-p',
                                 '--numb_person',
                                 default=10,
                                 type=int,
                                 dest='numb_person',
                                 help='An number of employees <default 10>')

        self.parser.add_argument('-t',
                                 '--numb_tasks',
                                 default=30,
                                 type=int,
                                 dest='numb_tasks',
                                 help='An number of tasks <default 30>')

    def parse(self, args=None):
        return self.parser.parse_args(args)
