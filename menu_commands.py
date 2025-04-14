from __future__ import annotations
from typing import Protocol
import menu
from task_service import TaskService

# from menu import MenuController

class MenuCommand(Protocol):
    def execute(self, controller):
        ...
    
    def get_name(self) -> str:
        ...

class CreateTask(MenuCommand):
    def execute(self, controller):
        title = controller.cli.prompt("Enter task title")
        description = controller.cli.prompt("Enter task description")
        controller.task_service.create_task(title, description)
        controller.current_menu = menu.MainMenu()
    
    def get_name(self) -> str:
        return "Create Task"

class ListTasks(MenuCommand):
    def execute(self, controller):
        tasks = controller.tasks
        if tasks:
            print("Tasks:")
            for task in tasks:
                print(f"- {task.title}")
        else:
            print("No tasks available.")
        controller.current_menu = menu.MainMenu()

    def get_name(self) -> str:
        return "List Tasks"

class ListDrafts(MenuCommand):
    def execute(self, controller):
        drafts = controller.drafts
        if drafts:
            print("Drafts:")
            for draft in drafts:
                print(f"- {draft.title}")
        else:
            print("No drafts available.")
        controller.current_menu = menu.MainMenu()

    def get_name(self):
        return "List Drafts"

class Exit(MenuCommand):
    def execute(self, controller):
        exit(0)
    
    def get_name(self) -> str:
        return "Exit"

class ReturnToMainMenu(MenuCommand):
    def execute(self, controller):
        controller.current_menu = menu.MainMenu()
    
    def get_name(self) -> str:
        return "Return To Main Menu"

class NotImplemented(MenuCommand):
    def __init__(self, message: str):
        self.message = message  

    def execute(self, controller):
        controller.current_menu = menu.MainMenu()

        
