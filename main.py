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
        self.tasks = {}

        try:
            with open(self.path, "r") as file_to_read:  
                self.tasks = json.load(file_to_read)
        except FileNotFoundError:
            print("invalid file path", f"creating a new empty json file")

    def add(self, task_name):
        status = {"status": "in-progress"}

        if task_name in self.tasks:
            self.tasks[task_name].append(status)
        else:
            self.tasks[task_name] = [status]

        self._id()

    def delete(self, task_name):
        if task_name in self.tasks:
            print(f"found task {task_name}")
        else:
            print(f"there is no task named {task_name}")

    def update(self, task_name):
        if task_name in self.tasks: 
            while True:
                print("Update Menu")
                print(" | ".join(self.statuses))

                update_command = input("update menu: ").lower()

                if any(command == update_command for command in self.statuses):
                    if update_command == "exit":
                        print("exiting the update menu")

                        return -1
                    else:
                        for task in self.tasks[task_name]:
                            if task["status"] != update_command:
                                task["status"] = update_command
                                
                                self._write()
                                return True
                            
                        print(f"All tasks have the status {update_command}")
                        return -1
                else:
                    print("unknown command try again")
        else:
            print('task not found')
            return -1

    def _id(self):
        for task_name, task_list in self.tasks.items():
            for index, task in enumerate(task_list):
                task["id"] = index + 1
                print(index, task)

        self._write()
        
    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

class CLI:
    def __init__(self):
        menu_options = ["add", "update", "delete", "search", "exit"]

        print("Welcome to Task Tracker CLI")

        while True:
            print("Main Menu")
            print("Menu Options:", " | ".join(menu_options))
            
            input_command = input("menu command: ").lower()

            if input_command == "exit":
                print("exiting the app")

                return
            
            if any(command == input_command for command in menu_options):      
                task_name = input("enter the task name: ")
                
                getattr(logic, input_command)(task_name)    
            else:
                print("invalid menu input try again")

                continue

logic = Logic()
cli = CLI()