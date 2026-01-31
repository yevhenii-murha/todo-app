def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todo_list = file.readlines()
    return todo_list


def write_todos(todo_list, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todo_list)
