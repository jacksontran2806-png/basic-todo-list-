task = []
def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

#add task to the list
def add_task():
    task_name = input("Enter task name: ")
    task.append({"task": task_name, "done": False})
    print(f"Task '{task_name}' added successfully!")

#view all the tasks in the list
def view_tasks():
    if not task:
        print("There are no tasks in the list.")
        return
    print("Tasks:")
    for index, item in enumerate(task, start=1):
        status = "Done" if item["done"] else "Not Done"
        print(f'{index}. {item["task"]} [{status}]')

#mark a task as done
def mark_task_done():
    view_tasks()
    if not task:
        return
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index <len(task):
            task[index]["done"] = True
            print(f"Task '{task[index]['task']}' marked as done! yeyeye!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#delete a task from the list
def delete_task():
    view_tasks()
    if not task:
        return
    try:
        index = int(input("Enter the task number to delete: ")) -1
        if 0 <= index < len(task):
            removed_task = task.pop(index)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("See you again, stay hard!")
        break
    else:
        print("Invalid choice. Please try again.") 
      


