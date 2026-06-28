import json
import pathlib
import os
from dotenv import load_dotenv

load_dotenv()

database = os.getenv("DATABASE")

class Logic:
    def __init__(self):
        self.path = pathlib.Path(__file__).parent.joinpath(database)
        self.statuses = ["done", "in-progress", "exit"]
        self.tasks = dict()

        try:
            with open(self.path, "r") as file_to_read:  
                self.tasks = json.load(file_to_read)
        except FileNotFoundError:
            print("invalid file path", f"created a new empty json file")

        if "tasks" not in self.tasks:
            self.tasks["tasks"] = list()

    def add(self):
        task_name = input("task name: ")
        
        self._setup()

        self.tasks["tasks"].append({"name": task_name, "status": "in-progress"})

        print(f"{task_name} was added to the task list")

        self._id()

    def update(self, task_id):
        for task in self.tasks["tasks"]:
            if task_id == task["id"]:
                while True:
                    print("leave blank to skip")
                    new_name = input("new name: ")
                    new_status = input("new status: ")

                    if new_name is not None:
                        task["name"] = new_name
                        
                    if new_status != "":
                            if new_status in self.statuses:
                                task["status"] = new_status
                                
                                self._write()

                                print(f"successfully updated task with id {task_id}")

                                return 1
                            else:
                                print("invalid status try again")

    def _id(self):
        for index, task in enumerate(self.tasks["tasks"]):
            task["id"] = index + 1

        self._write()

    def _setup(self):
        with open(self.path, "r") as file_to_read:  
            self.tasks = json.load(file_to_read)

        if "tasks" not in self.tasks:
            self.tasks["tasks"] = list()
        
    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

class CLI:
    def __init__(self):
        idless_menu_options = ["add", "exit"]
        menu_options = idless_menu_options

        menu_command = None
        task_id = None

        print("Welcome to Task Tracker CLI")

        while True:
            print("Main Menu")
            print("Menu Options:", " | ".join(menu_options))
            
            menu_command = input("menu command: ").lower()

            if menu_command not in menu_options:
                print("menu command must be in the list of menu options please try again")

                continue
            elif menu_command != "exit":
                if menu_command in idless_menu_options:
                    getattr(logic, menu_command)()
                else:
                    task_id = int(input("task id: "))

                    getattr(logic, menu_command)(task_id)
            else:
                print("exiting the app")

                return

logic = Logic()
cli = CLI()