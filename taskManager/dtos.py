class TaskDTO(object):

    def __init__(self, task_id, name, additional_info, priority, role, complete):
        self.task_id = task_id
        self.name = name
        self.additional_info = additional_info
        self.priority = priority
        self.role = role
        self.complete = complete


class EmployeeDTO(object):

    def __init__(self, employee_id, name, surname, role):
        self.employee_id = employee_id
        self.name = name
        self.surname = surname
        self.role = role
