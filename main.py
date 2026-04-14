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
            print("invalid file path", "creating a new empty json file: 'data.json'")

    def add(self, task_name):
        self.tasks[task_name] = {"status": "in-progress"}

        self._id()
        self._write()

    def update(self, task_id): 
        valid_update_inputs = ["done", "in-progress", "back"]

        for task_name, task_info in self.tasks.items():
            if task_id == task_info["id"]:
                print("Update Command Menu:\ndone\nin-progress\nback")

                while True:
                    status = input("Enter status: ")

                    if any(command in status for command in valid_update_inputs):
                        if status == "back":
                            print("redirecting to the main menu")
                            return

                        if status != task_info["status"]:
                            task_info.update({"status": status})
                            self._write()
                            return
                        else:
                            print(f"the status of {task_name} is already {status} please try again")
                    else:
                        print("task not found try again")
            
        print("task not found redirecting to the main menu")
    
    def delete(self):
        pass

    def _id(self):
        for index, key in enumerate(self.tasks):
            self.tasks[key].update({"id": index})

    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

    def _search_task(self, task_id):
        for task_name, task_info in self.tasks.items():
            if task_id == task_info["id"]:
                return True

class CLI:
    def __init__(self):
        print("Welcome to Task Tracker CLI")
        print("Command Menu\nadd\nupdate\ndelete\nexit:")

        valid_inputs = ["add", "update", "remove", "exit"]

        while True:
            command_input = input("command input: ").lower()
            
            valid = None

            if any(command in command_input for command in valid_inputs):
                valid = True
                
            if valid:   
                user_input = None

                if any(command in command_input for command in ["add"]):
                    user_input = input("Enter the task name: ")
                else:
                    user_input = int(input("Enter the task ID: "))
                
                if command_input == "add":
                    logic.add(user_input)
                elif command_input == "update":
                    logic.update(user_input)
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