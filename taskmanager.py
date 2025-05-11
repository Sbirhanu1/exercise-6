class Task:
    def __init__(self, title, level, deadline, is_done=False):
        self.title = title
        self.level = level
        self.deadline = deadline
        self.is_done = is_done

    def to_dict(self):
        return {
            "title": self.title,
            "level": self.level,
            "deadline": self.deadline,
            "is_done": self.is_done
        }

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task.is_done else "Not done"
            print(f"{i+1}. {task.title} | Level: {task.level} | Due: {task.deadline} | {status}")

def add_task(tasks):
    title = input("Task title: ")
    level = input("Difficulty level (1-5): ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    task = Task(title, level, deadline)
    tasks.append(task)
    print("Task added!")

def main():
    tasks = []

    while True:
        print("\n==== TASK MANAGER ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
