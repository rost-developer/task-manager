import sys
import names
from random import randint

from lib import Options
from lib import State
from lib import Employer
from lib import Task
from lib import Manager

if __name__ == '__main__':

    options = Options()
    opts = options.parse(sys.argv[1:])

    # Filling state employees
    state = State()

    for i in range(opts.numb_person):
        state.add_employer(Employer(names.get_full_name(), randint(8, 30)))

    # Filling list tasks
    task_list = [ Task("Task #{0}".format(i), randint(1, 8)) for i in range(opts.numb_tasks) ]

    # Distribution of tasks
    for task in task_list:
        Manager.appoint_task(state.state_getter, task)

    # Print result distribution
    for employer in state.state_getter:
        print("\n%s" % employer.__str__())