import os
import json
import pathlib
from dotenv import load_dotenv

load_dotenv()

database = os.getenv("DATABASE")

class Logic:
    def __init__(self):
        self.tasks = dict()
        
        if pathlib.Path(database).exists():
            with open(database, "r") as file:
                self.tasks = json.load(file)
        else:
            pathlib.Path(database).open("w").write(r"{}")

        if "task_list" not in self.tasks:
            self.tasks["task_list"] = []
            self._write()

    def add(self):
        task_name = input("task name\n")
        
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
        with open(database, "r") as file_to_read:  
            self.tasks = json.load(file_to_read)

        if "tasks" not in self.tasks:
            self.tasks["tasks"] = list()
        
    def _write(self):
        with open(database, "w") as database_file:
            json.dump(self.tasks, database_file, indent = 4)

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