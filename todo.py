tasks = []

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\n📋 Your Tasks:")
    for i, (task, done) in enumerate(tasks, 1):
        status = "☑ Done" if done else "× To be done"
        print(f"{i}. {task} - {status}")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append((task, False))  
        print("🆕 Task added!")
    else:
        print("⚠️ Task cannot be empty.")

def view_incompleted_tasks():
    incompleted = [(task, done) for (task, done) in tasks if not done]

    if not incompleted:
        print("🎉 All tasks are completed!")
        return

    print("\n⏳ Incompleted Tasks:")
    for i, (task, _) in enumerate(incompleted, 1):
        print(f"{i}. {task}")

def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    index = input("\n Enter task number to mark as completed: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(tasks):
            task, _ = tasks[index]
            tasks[index] = (task, True)
            print("✓ Task marked as completed.")
        else:
            print("⊘ Invalid task number.")
    else:
        print("⚠️ Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    index = input("\n Enter task number to delete: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(tasks):
            print(f"🗑️  Deleted: {tasks[index][0]}")
            tasks.pop(index)
        else:
            print("⊘ Invalid task number.")
    else:
        print("⚠️ Please enter a number.")


while True:
    print("\n ・・・・・・・・・・・・・・・・")
    print("        ✮ TO-DO LIST ✮     ")
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. View Incompleted Tasks")
    print("6. Exit")
    print("・・・・・・・・・・・・・・・・")

    choice = input("\n Enter a choice (1-6): ")

    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        mark_completed(tasks)
    elif choice == '4':
        delete_task(tasks)
    elif choice == '5':
        view_incompleted_tasks()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("\n Invalid option. Choose between 1-6.")
