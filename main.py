import json
import pathlib

path = pathlib.Path(__file__).parent / "data.json"
tasks = {}

def read():
    try:
        with open(path, "r") as file_to_read:
            return json.load(file_to_read)
    except FileNotFoundError:
        print("invalid file path", "creating a new empty json file: 'data.json'")
        return {}

def write():
    with open(path, "w") as file_to_write:
        json.dump(tasks, file_to_write, indent = 4)

tasks = read()

print("CLI Task Tracker")


while True:
    command = input("command: ").lower()

    if command == "exit":
        print("Exiting")
        break
    elif command == "show":
        print("Tasks")
        print(tasks)
    elif command == "add":
        print("New Task")

        new_task = input("name: ")

        if new_task == "":
            continue
        else:
            tasks[new_task] = "in progress"
            write()
    else:
        print("Did not understand the command. Try again.")