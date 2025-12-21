import json
from pathlib import Path
from .task import Task
class TodoList:
    def __init__(self, task: Task):
        self.task = Task()
        self.tasks_list = []

    def add(self, task: Task):
        self.tasks_list.append(task)

    def list(self):
        for task in self.tasks_list:
            return task

    def complete(self, task: Task):
        task.mark_completed()

    def delete(self, task: Task):
        del self.tasks_list[task]

    def save_to_json(self, filename: str):
        with open(Path(filename), 'w', encoding='utf-8') as file:
            json.dump(self.tasks_list, file)
    
    def load_from_json(self, filename: str):
        with open(Path(filename), 'r', encoding='utf-8') as file:
            load_info = json.load(file)
            return load_info
