from task import TaskContext, TaskDraft

class TaskService:
    def create_task(self, title: str, description: str):
        return TaskContext(TaskDraft(title, description))

    def edit_task(self, id: str, title: str, description: str):
        new_task_draft = TaskDraft(title, description, id)
        new_task_draft.save()
        
