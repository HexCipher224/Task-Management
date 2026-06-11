from datetime import datetime

# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date) :
        new_task = {
            "title" :  title.strip(),
            "description": description.strip(),
            "due_date": due_date.strip(),
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
    else:
        print("Failed to add task due to validation errors.")
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index) - 1
        if 0 <= idx < len(tasks) :
            tasks[idx] ["completed"] = True
            print("Task marked as complete!")
        else :
            print("Invalid task number.")
    except ValueError:
        print("Please provide a valid numeric index.")

    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    print("\n--- Pending Tasks ---")
    has_pending = False

    for i, task in enumerate(tasks) :
        if not task["completed"] :
            print(f"{i + 1}. Title: {task['title']} | Due: {task['due_date']}")
            print(f"  Description: {task["description"]}")
            has_pending = True

        if not has_pending:
            print("No pending task found!")
# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    total_tasks = len(tasks)
    completed_count = sum(1 for task in tasks if task["completed"])

    progress = (completed_count / total_tasks) * 100
    return progress