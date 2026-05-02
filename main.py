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
        else:
            print("loaded data.json")

    def add(self, task_name):
        for key in self.tasks.keys():
            if task_name == key:
                self.tasks[task_name].append({"status": "in-progress"})

                self._write()
                return

        self.tasks[task_name] = list()
        self.tasks[task_name].append({"status": "in-progress"})

        self._write()

    def update(self, task_name): 
        valid_update_inputs = ["done", "in-progress", "back", "rename"]

        for task_name, task_info in self.tasks.items():
            print(task_name, task_info)

            # if task_id == task_info["id"]:
            #     print("Update Command Menu:\ndone\nin-progress\nback")

            #     while True:
            #         status = input("Enter status: ")

            #         if any(command in status for command in valid_update_inputs):
            #             if status == "back":
            #                 print("redirecting to the main menu")
            #                 return

            #             if status != task_info["status"]:
            #                 task_info.update({"status": status})
            #                 self._write()
            #                 return
            #             else:
            #                 print(f"the status of {task_name} is already {status} please try again")
            #         else:
            #             print("task not found try again")
            
        print("task not found redirecting to the main menu")
    
    def delete(self, task_id):
        for task_name, task_info in self.tasks.items():
            if task_id == task_info["id"]:
                while True:
                    confirmation = input(f"delete task (yes / no) {task_name}? ")

                    if confirmation == "yes":
                        self.tasks.pop(task_name)
                        self._write()
                        return
                    elif confirmation == "no":
                        return
                    else:
                        print("invalid input please try againn")

        print("task not found")
        return

    # def _id(self):
    #     for index, key in enumerate(self.tasks): 
    #         self.tasks[key].update({"id": index})

    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

    def _search_task(self, task_id):
        for task_name, task_info in self.tasks.items():
            if task_id == task_info["id"]:
                return True

class CLI:
    def __init__(self):
        valid_menu_inputs = ["add", "update", "delete", "search", "exit"]

        print("Welcome to Task Tracker CLI")
        print("Menu Inputs:", f", ".join(valid_menu_inputs))

        while True:
            command_input = input("command input: ").lower()
            
            if any(command in command_input for command in valid_menu_inputs):                
                    user_input = None

                    if any(command in command_input for command in ["add"]):
                        user_input = input("enter the task name: ")

                        self._commands(user_input, command_input)
                    else:
                        self._commands(user_input, command_input)
            else:
                print("invalid menu input try again")

    def _commands(self, user_input, command_input):
        if command_input == "add":
            logic.add(user_input)
        elif command_input == "update":
            logic.update(user_input)
        elif command_input == "delete":
            logic.delete(user_input)
        elif command_input == "exit":
            print("exiting the task tracker")
            return

logic = Logic()
cli = CLI()

# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress