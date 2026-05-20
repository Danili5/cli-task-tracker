import json
import pathlib

class Logic:
    def __init__(self):
        self.path = None
        self.tasks = None

        file_name = input("filename: ")

        if file_name == "":
            file_name = None

        if file_name is None:
            self.path = pathlib.Path(__file__).parent / "data.json"
        else:
            self.path = pathlib.Path(__file__).parent / file_name

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

    def _task_exists(self, task_name):
        for task in self.tasks:
            if task == task_name:
                return True

        return False

    def update(self, task_name):
            if self._task_exists:
                update_options = ["done", "not done", "in-progress"]
                print("Update Options: ", " | ".join(update_options))

                while True:
                    input_command = input("update command: ").lower()

                    if any(command == input_command for command in update_options):
                        for task in self.tasks[task_name]:
                            if task["status"] != input_command:
                                task["status"] = input_command

                                self._write()

                                break

                        break
                    else:
                        print(f"{input_command} is unknown try again")
            else:
                print(f"{task_name} not found")
    
    def delete(self, task_name):
        print(task_name)

        # for task_name, task_info in self.tasks.items():
        #     if task_id == task_info["id"]:
        #         while True:
        #             confirmation = input(f"delete task (yes / no) {task_name}? ")

        #             if confirmation == "yes":
        #                 self.tasks.pop(task_name)
        #                 self._write()
        #                 return
        #             elif confirmation == "no":
        #                 return
        #             else:
        #                 print("invalid input please try againn")

        # print("task not found")
        # return

    # def search(self, task_name):
    #     print("search function")

    def _write(self):
        with open(self.path, "w") as file_to_write:
            json.dump(self.tasks, file_to_write, indent = 4)

    # def _search_task(self, task_id):
    #     for task_name, task_info in self.tasks.items():
    #         if task_id == task_info["id"]:
    #             return True

class CLI:
    def __init__(self):
        menu_options = ["add", "update", "delete", "search"]

        print("Welcome to Task Tracker CLI")
        print("Menu Options:", " | ".join(menu_options))

        while True:
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