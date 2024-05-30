import time

import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
FILEPATH = "todos.txt"
print(time.strftime("%d-%b,%Y"))


def read_todo(filepath=FILEPATH):
    """This function is for reading the file from text doc"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_1:
        file_1.writelines(todos_arg)


if __name__ == "__main__":
    print("I am micky from functions")

    print(read_todo())
