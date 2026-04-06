import json
import pathlib

class Logic:
    def __init__(self):
        self.path = pathlib.Path(__file__).parent / "data.json"
        self.tasks = None

        try:
            with open(self.path, "r") as file_to_read:
                self.tasks = json.load(file_to_read)
        except FileNotFoundError:
            print("invalid file path", "creating a new empty json file: 'data.json'")
            self.tasks = {}

    def add(self, task_name):
        self.tasks[task_name] = {"status": "in-progress"}

        self._id()
        self._write()

    def update(self):
        pass
    
    def delete(self):
        pass

    def _id(self):
        for index, key in enumerate(self.tasks):
            self.tasks[key].update({"id": index})

    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

    def _search_task(self, task_name_search):
        for task_name in self.tasks.keys():
            if task_name_search == task_name:
                print("found task", task_name) 

class CLI:
    def __init__(self):
        print("Welcome to Task Tracker CLI")
        print("Command Menu\nadd\nupdate\ndelete\nexit")

        valid_inputs = ["add", "update", "remove", "exit"]

        while True:
            command_input = input("command input: ").lower()
            
            valid = None

            for valid_input in valid_inputs:
                if command_input == valid_input:
                    valid = True
                    break
                
                valid = False
                
            if valid:   
                task_name = input("task name: ")
                
                if command_input == "add":
                    logic.add(task_name)
                elif command_input == "update":
                    self._search_task(task_name)
                elif command_input == "exit":
                    break
            else:
                print("invalid input try again")

logic = Logic()
cli = CLI()

# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

# path = pathlib.Path(__file__).parent / "data.json"
# tasks = {}

# def read():
    

# def write():
#     with open(path, "w") as file_to_write:
#         json.dump(tasks, file_to_write, indent = 4)

# tasks = read()

# print("CLI Task Tracker\ncommands:\nexit\nshow\nadd\nupdate")