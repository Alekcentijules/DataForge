from pathlib import Path
from typing import List, Dict, Any
import json
from .task import Task
from .utils import CustomError

class TodoList:

    DEFAULT_FILE = Path('data/tasks.json')

    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self._next_id = 1

    def add(self, title: str, description: Optional[str] = None) -> None:
        if not title:
            raise CustomError('Title cannot be empty.')
        task = Task(
            id=self._next_id,
            title=title,
            description=description
        )
        self.tasks.append(task)
        self._next_id += 1

    def list_tasks(self) -> None:
        if not self.tasks:
            return 'No tasks yet.'
        return '\n'.join(str(task) for task in self.tasks)

    def complete_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return
        raise CustomError('Task not found.')

    def delete_task(self, task: Task):
        initial_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) == initial_length:
            raise CustomError('Task not found.')

    def save_to_json(self, filename: str | Path = DEFAULT_FILE):
        Path(filename).parent.mkdir(exist_ok=True)
        data = [task.to_dict() for task in self.tasks]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def load_from_json(self, filename: str):
        try:
            with open(Path(filename), 'r', encoding='utf-8') as file:
                data = json.load(file)
            self.tasks = [Task.from_dict(item) for item in data]
            self._next_id = max(task.id for task in self.tasks) + 1 if self.tasks else 1    
        except FileNotFoundError:
            pass