'''
Task Class for To Do
'''
class Task():
    # Constructor
    def __init__(self, description="", completed=False):
        self.description = description 
        self.completed = completed 

    # Boolean to check if completed
    def mark_complete(self):
        self.completed = True

    # Edit task description
    def edit(self, new_descript):
        self.description = new_descript

    # String representation
    def __str__(self):
        return f"Description: {self.description}\nCompleted: {self.completed}"
