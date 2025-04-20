class Task:
    def __init__(self, title, level, deadline, is_done=False):
        self.title = title           
        self.level = level           
        self.deadline = deadline     
        self.is_done = is_done       

    def to_dict(self):
        task_info = {"title": self.title,"level": self.level,"deadline": self.deadline,"is_done": self.is_done}
        return task_info