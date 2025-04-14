from task import TaskContext, TaskDraft

class TaskService:
    def create_task(self, title: str, description: str):
        return TaskContext(TaskDraft(title, description))
        
