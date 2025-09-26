'''
To-Do class
1 add task
2 remove task
3 edit a task
4 mark task complete
5 view specific task -> goes to all tasks and choose?
5 view all uncompleted tasks
6 view all completed tasks
7 view all tasks
8 sort?
9 clear all
10 exit
'''

import json
from task import Task

class toDo():
    # Constructor
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_file()

    # Helper method, this honestly might be unnecessary as it checks in the main file
    def check_numberExc(self, index):
        # Returns True if index is within range of task list
        return 0 <= index < len(self.tasks)

    # Main methods
    
    # Add function will add the task
    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_file()

    # Remove function will delete the task
    def remove_task(self, index):
        if self.check_numberExc(index):
            del self.tasks[index]
            self.save_file()

    # Edit function will change the task description
    def edit_task(self, index, new_description):
        if self.check_numberExc(index):
            self.tasks[index].edit(new_description)
            self.save_file()

    # Mark function will set a task as complete
    def mark_complete(self, index):
        if self.check_numberExc(index):
            self.tasks[index].mark_complete()
            self.save_file()
    
    # View completed tasks
    def get_completed_tasks(self):
        completed_tasks = []
        # Loop through tasks and add completed ones to list
        for t in self.tasks:
            if t.completed:
                completed_tasks.append(t)
        return completed_tasks

    # View uncompleted tasks
    def get_uncompleted_tasks(self):
        uncompleted_tasks = []
        # Loop through tasks and add uncompleted ones to list
        for t in self.tasks:
            if not t.completed:
                uncompleted_tasks.append(t)
        return uncompleted_tasks
    
    # View all tasks
    def get_all_tasks(self):
        all_tasks = []
        # Loop through tasks and add to list
        for t in self.tasks:
            all_tasks.append(t)
        return all_tasks

    # Clear function will remove all tasks
    def clear_all(self):
        self.tasks.clear()
        self.save_file()

    # Sort if I have extra time
    def sort(self):
        pass

    # Save tasks to JSON file
    def save_file(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(
                    [{"description": t.description, "completed": t.completed} for t in self.tasks],
                    f,
                    indent=4
                )
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    # Load tasks from JSON file
    def load_file(self):
        try:
            print("Loading saved tasks...")
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task(d["description"], d["completed"]) for d in data]
            print(f"{len(self.tasks)} tasks loaded.")
        except FileNotFoundError:
            print("No saved tasks found. Starting fresh.")
            self.tasks = []
        except json.JSONDecodeError:
            print("Error: tasks file is corrupted. Starting with an empty list.")
            self.tasks = []
        except Exception as e:
            print(f"Unexpected error while loading tasks: {e}")
            self.tasks = []

