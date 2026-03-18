# Jordan Fitzgerald
# 3/18/2026
# To Do List:

tasks = []

while True:
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # View tasks
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks added yet.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        pass

    elif choice == "2":
        # Add task
        task = input("Enter a new task:")
        tasks.append(task)
        print(f"Added task: {task}")
        pass

    elif choice == "3":
        # Delete task
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks): 
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid Task Number")
        pass

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
