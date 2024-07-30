
filepath = "todo.txt"


def get_todos(filename: str = filepath) -> list:
    """
     Function takes filepath and reads the given file and return the file data as a list
    :param filename:
    :return: List:Data
    """
    with open(filename, 'r') as fi_:
        data = fi_.readlines()
        return data


def write_file(todo_,filepath_=filepath):
    with open(filepath_, 'w') as f:
        f.writelines(todo_)
