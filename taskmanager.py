class Task:
    def __init__(self, title, level, deadline, is_done=False):
        self.title = title
        self.level = level
        self.deadline = deadline
        self.is_done = is_done

    def to_dict(self):
        task_info = {
            "title": self.title,
            "level": self.level,
            "deadline": self.deadline,
            "is_done": self.is_done
        }
        return task_info

    def __str__(self):
        status = "Done" if self.is_done else "Not Done"
        return f"{self.title} - {self.level} - Due: {self.deadline} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, level, deadline):
        new_task = Task(title, level, deadline)
        self.tasks.append(new_task)
        print("Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")


def main():
    manager = TaskManager()
    while True:
        print("\nTASK MANAGER")
        print("1. View tasks")
        print("2. Add task")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            manager.view_tasks()
        elif choice == "2":
            title = input("Title: ")
            level = input("Level: ")
            deadline = input("Deadline: ")
            manager.add_task(title, level, deadline)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid option.")


if __name__ == '__main__':
    main()
