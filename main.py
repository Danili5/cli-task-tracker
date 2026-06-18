import json
import pathlib

class Logic:
    def __init__(self):
        self.path = pathlib.Path(__file__).parent / "data.json"
        self.tasks = {}

        try:
            with open(self.path, "r") as file_to_read:  
                self.tasks = json.load(file_to_read)
        except FileNotFoundError:
            print("invalid file path", f"creating a new empty json file: {file_name}")

    def add(self, task_name):
        status = {"status": "not done"}

        if task_name in self.tasks:
            self.tasks[task_name].append(status)
        else:
            self.tasks[task_name] = [status]

        self._write()

    # requires debugging
    def update(self, task_name):
        if task_name in self.tasks: 
            update_options = ["done", "not done", "postpone", "exit"]

            while True:
                print("Update Menu")
                print(" | ".join(update_options))

                input_command = input("update menu: ").lower()

                if any(command == input_command for command in update_options):
                    if input_command == "exit":
                        return -1
                    else:
                        for task in self.tasks[task_name]:
                            if task["status"] != input_command:
                                task["status"] = input_command
                                self._write()
                                return True
                            
                            print(f"All tasks have the status {input_command}")
                            return -1
                else:
                    print("unknown command try again")
        else:
            print('not found')
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

# Add (completed), Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress