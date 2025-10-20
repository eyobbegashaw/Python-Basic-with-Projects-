# Simple to-do list application
todo_list = []

def add_task(task, priority="medium"):
    """Add task to to-do list"""
    todo_list.append({
        "task": task,
        "priority": priority,
        "completed": False
    })

def complete_task(task_index):
    """Mark task as completed"""
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        return True
    return False

def view_tasks(show_completed=True):
    """Display tasks"""
    if not todo_list:
        print("No tasks in the list!")
        return
    
    print("\n📝 To-Do List:")
    print("-" * 50)
    
    for i, task in enumerate(todo_list):
        if not show_completed and task["completed"]:
            continue
            
        status = "✅" if task["completed"] else "⏳"
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}[task["priority"]]
        
        print(f"{i+1}. {status} {priority_icon} {task['task']}")

# Usage
add_task("Learn Python lists", "high")
add_task("Buy groceries", "medium")
add_task("Read a book", "low")

complete_task(0)  # Complete first task
view_tasks()