# Import functions from task_manager.task_utils package
None
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n--- Add a New Task ---")
            title = input("Enter title: ")
            description = input(" Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            view_pending_tasks()
            index_input = input("\nEnter the number of the task to complete: ")
            mark_task_as_complete(index_input)

        elif choice == "3":
            view_pending_tasks()
        
        elif choice == "4":
            current_progress = calculate_progress()
            print(f"\nYour current progress: {current_progress:.1f}% complete.")

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
