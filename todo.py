tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print("Task added!")

def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        num = int(input("Enter task number to remove: "))
        remove_task(num)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
