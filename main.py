import json
import pathlib
import os
from dotenv import load_dotenv

load_dotenv()

data_file = os.getenv("DATA")

print(data_file)

class Logic:
    def __init__(self):
        self.path = pathlib.Path(__file__).parent.joinpath(data_file)
        self.update_menu = ["done", "in-progress", "exit"]
        self.tasks = {}

        try:
            with open(self.path, "r") as file_to_read:  
                self.tasks = json.load(file_to_read)
        except FileNotFoundError:
            print("invalid file path", f"creating a new empty json file: {file_name}")

    def add(self, task_name):
        status = {"status": "in-progress"}

        if task_name in self.tasks:
            self.tasks[task_name].append(status)
        else:
            self.tasks[task_name] = [status]

        self._write()

    def update(self, task_name):
        if task_name in self.tasks: 
            while True:
                print("Update Menu")
                print(" | ".join(self.update_menu))

                update_command = input("update menu: ").lower()

                if any(command == update_command for command in self.update_menu):
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

    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

class CLI:
    def __init__(self):
        menu_options = ["add", "update", "delete", "search"]

        print("Welcome to Task Tracker CLI")

        while True:
            print("Main Menu")
            print("Menu Options:", " | ".join(menu_options))
            
            input_command = input("menu command: ").lower()
            
            if any(command == input_command for command in menu_options):      
                task_name = input("enter the task name: ")
          
                getattr(logic, input_command)(task_name)    
            elif input_command == "exit":
                print("exiting the app")

                break
            else:
                print("invalid menu input try again")

                continue

logic = Logic()
cli = CLI()

# Add (completed), Update (complete), and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress