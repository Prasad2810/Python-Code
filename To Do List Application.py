import json

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

def list_tasks(tasks):
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        action = input("Enter 'add' to add a task, 'list' to view tasks, or 'quit' to exit: ")
        if action == 'add':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif action == 'list':
            list_tasks(tasks)
        elif action == 'quit':
            break
        else:
            print("Invalid action.")