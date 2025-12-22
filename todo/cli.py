from .task import Task
from .utils import input_errors
from .todo_list import TodoList
from typing import Tuple, List

@input_errors
def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.strip().split()
    if not parts:
            return ()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args
class CLI:
    @input_errors
    def add_task(args: list, todo: TodoList):
        id = int(args[0])
        title = args[1]
        description = args[2]
        created_at = args[3] if description else args[2]
        if title not in todo:
            task = Task(id=id, title=title, description=description, created_at=created_at)
            todo.add(task)
            messege = 'Task added.'
        else:
            messege = 'Task was in list.'
        return messege

    @input_errors
    def show_list(args: list, todo: TodoList):
        return todo.list()

    @input_errors
    def delete_task(args: list, todo: TodoList):
        task = Task(*args)
        return todo.delete(task)

    @input_errors
    def complete_task(args: list, todo: TodoList):
        task = Task(*args)
        return todo.complete(task)

    COMMANDS = {
        'add': add_task,
        'list': show_list,
        'delete': delete_task,
        'complete': complete_task
    }

@input_errors
def run():
    while True:
        todo = TodoList()
        user_input = input('Enter a command: ')

        if not user_input:
            print('Enter a command, please: ')
            continue

        cmd, args = parse_input(user_input)
        cli = CLI()
        commands = cli.COMMANDS

        if cmd not in commands:
            print('Enter a correct command, please: ')
            continue
        
        result = commands[cmd](args, todo)
        print(result)

        if commands in ('close', 'exit'):
            todo.save_to_json()
            break
            
