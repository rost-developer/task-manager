class Manager(object):

    @staticmethod
    def appoint_task(state_list, task_object):
        """
        This function distributes the tasks between employees
        With parameters state - list employees object , task_object - task object
        """
        for employee in sorted(state_list, key=lambda empl: empl.total_point_getter, reverse=False):
            if employee.is_ready_get_task(task_object.task_point_getter):
                employee.add_task(task_object)
                break
