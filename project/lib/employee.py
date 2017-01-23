import json


class Employee(object):
    """
    this class is useful for defining a type of Employer
    with its nick name, personal point, total point, tasks
    this class has following methods and properties
       add_task()
       is_ready_get_task()
       nick_name_getter()
       personal_point_getter()
       list_task_getter()
       total_point_getter()
    """

    def __init__(self, nick_name, personal_point):
        self._nickName = nick_name
        self._personal_point = personal_point
        self._list_task = []
        self._total_point = 0

    def add_task(self, task_object):
        self._total_point += task_object.task_point_getter
        self._list_task.append(task_object)

    @property
    def nick_name_getter(self):
        return self._nickName

    @property
    def personal_point_getter(self):
        return self._personal_point

    @property
    def list_task_getter(self):
        return self._list_task

    @property
    def total_point_getter(self):
        return self._total_point

    def is_ready_get_task(self, task_point):
        """
        this function checking ready get new tasks
        """
        if self._personal_point > self._total_point + task_point:
            return True
        else:
            return False

    def __str__(self, type_format=None):
        if type_format == 'json':
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=False, indent=4)

        return "Name: {0}\nPersonal Point: {1}\nTotal Point: {2}\nCount Task: {3}\nTasks: \n[{4}\n]" \
            .format(self._nickName, str(self._personal_point), str(self._total_point), len(self._list_task),
                    ' '.join(task.__str__() for task in self._list_task))
