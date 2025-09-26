from to_do import toDo

# Helper function

# Get a yes/no response from user
def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().upper()
        if choice in ("Y", "N"):
            return choice
        print("Invalid input! Please enter Y or N.")

# Add a new task
def add_task_prompt(todo):
    choice = get_yes_no("Add a new task? (Y/N): ")
    if choice.upper() == "Y":
        description = input("Enter task description: ").strip()
        if not description:  # Catch empty string or just spaces
            print("Task description cannot be empty!")
            return
        try:
            todo.add_task(description)
            print("Task added!")
        except ValueError:
            print("Invalid input! Please try again.")
            return
    else:
        return looping_prompt(todo)

# Edit an existing task
def edit_task_prompt(todo):
    choice = get_yes_no("Edit a task? (Y/N): ")

    if choice.upper() == "Y":
        # Show all tasks before editing
        for i, task in enumerate(todo.get_all_tasks(), start=1):
            print(f"{i}) {task}")

        try:
            index = int(input("Select task number to edit: ")) - 1  # Convert to 0-based index
            
            # Check if index is valid
            if index < 0 or index >= len(todo.tasks):
                print("Invalid task number!")
                return
            
            # Prompt for new description
            new_description = input("Enter new description: ").strip()
            if not new_description:
                print("Task description cannot be empty!")
                return

            # Edit the task
            todo.edit_task(index, new_description)
            print("Task updated!")
        except (ValueError, IndexError):
            print("Invalid input! Please try again.")
            return
    else:
        return looping_prompt(todo)

# Remove a task
def remove_task_prompt(todo):
    # Show all tasks before removing
    for i, task in enumerate(todo.get_all_tasks(), start=1):
        print(f"{i}) {task}")

    try:
        index = int(input("Select task number to remove: ")) - 1

        # Check if index is valid
        if index < 0 or index >= len(todo.tasks):
            print("Invalid task number!")
            return

        # Warn if task is not completed yet
        if not todo.tasks[index].completed:
            confirm = get_yes_no("Task is not completed. Are you sure you want to remove it? (Y/N): ")
            if confirm == "N":
                print("Task not removed.")
                return
            else:
                # Remove the task
                todo.remove_task(index)
                print("Task removed!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Mark a task as complete
def mark_task_prompt(todo):
    # Show all tasks before marking complete
    for i, task in enumerate(todo.get_all_tasks(), start=1):
        print(f"{i}) {task}")

    try:
        index = int(input("Select task number to mark complete: ")) - 1

        # Check if index is valid
        if index < 0 or index >= len(todo.tasks):
            print("Invalid task number!")
            return

        if todo.tasks[index].completed:
            print("Task is already marked complete!")
            return

        todo.mark_complete(index)
        print("Task marked complete!")
    except (ValueError, IndexError):
        print("Invalid input! Please try again.")
        return

# View tasks menu
def view_task_prompt(todo):
    while True:
        view_choice = input(
            "View:\n"
            "\t1) All Tasks\n"
            "\t2) Completed Tasks\n"
            "\t3) Uncompleted Tasks\n"
            "\t4) Back to Main Menu\n>>> "
        ).strip()

        if view_choice == "1":
            print("\nAll Tasks:")
            for task in todo.get_all_tasks():
                print(task)
        elif view_choice == "2":
            print("\nCompleted Tasks:")
            for task in todo.get_completed_tasks():
                print(task)
        elif view_choice == "3":
            print("\nUncompleted Tasks:")
            for task in todo.get_uncompleted_tasks():
                print(task)
        elif view_choice == "4":
            break
        else:
            print("Invalid choice! Please enter 1–4.")
        
# Clear all tasks
def clear_all(todo):
    confirm = input("Are you sure you want to clear all tasks? (Y/N): ").strip()
    if confirm.upper() == "Y":
        todo.tasks.clear()
        todo.save_file()
        print("All tasks cleared!")
    else:
        looping_prompt(todo)

# Main looping prompt
def looping_prompt(todo):
    while True:
        try:
            userChoice = int(input(
                "\nSelect what to do:\n"
                "\t1) Add a new task\n"
                "\t2) Edit a task\n"
                "\t3) Remove a task\n"
                "\t4) Mark a task complete\n"
                "\t5) View tasks\n"
                "\t6) Clear all tasks\n"
                "\t7) Exit\n>>> "
            ))
        except ValueError:
            print("Invalid input! Please enter a number 1–7.")
            continue

        if userChoice == 1:
            add_task_prompt(todo)
        elif userChoice == 2:
            edit_task_prompt(todo)
        elif userChoice == 3:
            remove_task_prompt(todo)
        elif userChoice == 4:
            mark_task_prompt(todo)
        elif userChoice == 5:
            view_task_prompt(todo)
        elif userChoice == 6:
            clear_all(todo)
        elif userChoice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1–7.")

# Entry point
def main():
    todo = toDo()
    print("Welcome to your personal To-Do List!")
    looping_prompt(todo)
    

if __name__ == "__main__":
    main()