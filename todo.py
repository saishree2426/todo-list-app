"""
To-Do List Application (Console-based)
A simple CLI to-do manager that persists tasks to a text file.
"""

import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Read tasks from the text file into a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        # Strip newline characters, ignore blank lines
        return [line.strip() for line in f.readlines() if line.strip()]


def save_tasks(tasks):
    """Write the current list of tasks back to the text file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def view_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks yet. Add one!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("------------------------\n")


def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Added: "{task}"\n')
    else:
        print("Task cannot be empty.\n")


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f'Removed: "{removed}"\n')
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def show_menu():
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List App!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Your tasks are saved in tasks.txt")
            break
        else:
            print("Invalid option. Please choose 1-4.\n")


if __name__ == "__main__":
    main()
