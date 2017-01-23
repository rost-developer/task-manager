class Task(object):
    """
    this class is useful for defining a type of Task
    with its task name and task point
    this class has following methods and properties
        task_id_getter()
        task_point_getter()
    """

    def __init__(self, task_name, task_point):
        self._task_name = task_name
        self._task_point = task_point

    @property
    def task_name_getter(self):
        return self._task_name

    @property
    def task_point_getter(self):
        return self._task_point

    def __str__(self):
        return "\n\tTask Name: {0}\n\tTask Point: {1}\n".format(self._task_name, self._task_point)