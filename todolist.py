def task():
    tasks = []  # empty list
    print("Welcome to the Task Management System")
    total_task = int(input("Enter how many tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print("Today's tasks are:")
    for t in tasks:
        print("-", t)

    while True:
        operation = int(input("\nEnter operation:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nChoice: "))
        
        if operation == 1:  # Add
            add = input("Enter a task to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added.")

        elif operation == 2:  # Update
            update_value = input("Enter the task you want to update: ")
            if update_value in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(update_value)
                tasks[ind] = up
                print(f"'{update_value}' has been updated to '{up}'.")
            else:
                print("The task you want to update is not present.")

        elif operation == 3:  # Delete
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"'{del_val}' has been deleted.")
            else:
                print("The task you want to delete is not present.")

        elif operation == 4:  # View
            print(f"\nCurrent total tasks: {len(tasks)}")
            for t in tasks:
                print("-", t)

        elif operation == 5:  # Exit
            print("Closing the program.")
            break

        else:
            print("Invalid input.")
task()
