import json


class State(object):
    """
    this class is useful for defining a type of State (Stuff)
    this class has following methods and properties
       add_employee( Object Employee)
       count_employee()
       nick_name_getter()
       exists_employee(nick_name)
       search_employee(nick_name)
       state_getter()
    """
    def __init__(self):
        self._list_employee = []

    def add_employee(self, employee):
        self._list_employee.append(employee)

    def count_employee(self):
        return len(self._list_employee)

    def exists_employee(self, nick_name):
        return True if any(employee.nick_name_getter == nick_name for employee in self._list_employee) else False

    def search_employee(self, nick_name):
        search = [employee for employee in self._list_employee if employee.nick_name_getter == nick_name]
        if search:
            return search[0]
        return False

    @property
    def state_getter(self):
        return self._list_employee

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)