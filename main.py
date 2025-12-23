from task import Task
from todo_list import TodoList

def main() -> None:
    todo = TodoList()
    todo.load_from_json()
    print('Welcom to CLI Todo List!')

    cli = CLI(todo)
    cli.run()

    todo.save_to_json()
    print('Goodbuy! Tasks saved.')

if __name__ == '__main__':
    main()
