import os

PLANNER_FILE = "planner.txt"

def show_menu():
    print("\n🗓️ Daily Planner")
    print("1. View schedule")
    print("2. Add task")
    print("3. Remove task")
    print("4. Clear all tasks")
    print("5. Exit")

def load_tasks():
    if not os.path.exists(PLANNER_FILE):
        return []
    with open(PLANNER_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(PLANNER_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_schedule():
    tasks = load_tasks()
    if not tasks:
        print("Your schedule is empty.")
    else:
        print("\nToday's Schedule:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    time = input("Enter time (e.g., 7:00 AM): ")
    activity = input("Enter task description: ")
    print("Choose a category:")
    print("1. Work\n2. Personal\n3. Urgent\n4. Everyday")
    category_map = {"1": "Work", "2": "Personal", "3": "Urgent", "4": "Everyday"}
    category_choice = input("Enter category number (1-4): ")
    category = category_map.get(category_choice, "Uncategorized")
    tasks = load_tasks()
    tasks.append(f"{time} - {activity} [{category}]")
    save_tasks(tasks)
    print("Task added!")

def remove_task():
    tasks = load_tasks()
    view_schedule()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        save_tasks([])
        print("All tasks cleared.")
    else:
        print("Clear cancelled.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            view_schedule()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
