class TaskDTO(object):

    def __init__(self, task_id, name, additional_info, priority, complete):
        self.task_id = task_id
        self.name = name
        self.additional_info = additional_info
        self.priority = priority
        self.complete = complete


class WorkerDTO(object):

    def __init__(self, worker_id, name, surname, role):
        self.worker_id = worker_id
        self.name = name
        self.surname = surname
        self.role = role
