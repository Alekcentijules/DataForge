from datetime import datetime

class Task:
    def __init__(self, id: int, title: str, description: None, completed: False, created_at) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now()

    def mark_completed(self):
        self.complete = True

    def str(self):
        status = '[x]' if self.complete == True else ''
        desc = f" - {self.description}" if self.description else ''
        data = self.created_at.strftime('%d-%m-%Y')
        return f'{self.id} {status} {self.title}{desc} (created: {data})'
        
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_ad': self.created_at
        }
    
    @classmethod
    def from_dict(clm, data: dict) -> 'Task':
        created_at = datetime.fromisoformat(data['created_at'])
        return clm(
            id=data['id'],
            title=data['title'],
            description=data.get('description'),
            complete=data['complete'],
            created_at=created_at
        )
