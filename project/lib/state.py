import json


class State(object):
    def __init__(self):
        self._list_employer = []

    def add_employer(self, employer):
        self._list_employer.append(employer)

    def count_employer(self):
        return len(self._list_employer)

    def exists_employer(self, nick_name):
        return True if any(d.nick_name_getter == nick_name for d in self._list_employer) else False

    def search_employer(self, nick_name):
        search = [employer for employer in self._list_employer if employer.nick_name_getter == nick_name]
        if search:
            return search[0]
        return False

    @property
    def state_getter(self):
        return self._list_employer

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)