from datetime import datetime

def validate_task_title(title):
    if title.strip () == "" :
        print("Validation Error: Task title cannot be empty!")
        return False
    return True
    
def validate_task_description(description):
    if description.strip() == "" :
        print("Validation Error: Task description cannot be empty!")
        return False
    return True
    
def validate_due_date(due_date):
    try: 
        datetime.strptime(due_date.strip(), "%Y-%M-%D")
        return True
    except ValueError:
        print("Validation Error: Invalid date format! Please use YYYY-MM-DD")
        return False
    