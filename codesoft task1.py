import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. {task.title} - {task.description} ({status})")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = True

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            task_list = [{'title': task.title, 'description': task.description, 'completed': task.completed} for task in self.tasks]
            json.dump(task_list, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            task_list = json.load(f)
            self.tasks = [Task(task['title'], task['description']) for task in task_list]

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Application =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '5':
            filename = input("Enter file name to save tasks: ")
            todo_list.save_to_file(filename)
        elif choice == '6':
            filename = input("Enter file name to load tasks: ")
            todo_list.load_from_file(filename)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()
