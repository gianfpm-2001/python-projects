# To-Do List App

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed: {task}")
    else:
        print("Task not found")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

add_task("Learn Python")
add_task("Build a project")
add_task("Apply for jobs")
show_tasks()
remove_task("Learn Python")
show_tasks()
