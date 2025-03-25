todo_list = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not todo_list:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove!")
        else:
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_num < len(todo_list):
                    removed_task = todo_list.pop(task_num)
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
