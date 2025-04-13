from typing import List, Protocol
from menu_commands import CreateTask, Exit, ListDrafts, ListTasks, MenuCommand
from task import Task, TaskDraft


class Menu(Protocol):
    def get_commands(self) -> List[MenuCommand]:
       ...

class MainMenu(Menu):
    def get_commands(self) -> List[MenuCommand]:
        return [
            CreateTask(),
            ListTasks(),
            ListDrafts(),
            Exit()
        ]

class MenuController:
    def __init__(self, tasks: list[Task], drafts: list[TaskDraft]) -> None:
        self.current_menu = MainMenu()
        self.tasks = tasks
        self.drafts = drafts
        
    def display_menu(self) -> str:
        choices = self.current_menu.get_commands()
        return "\n".join(f"{idx + 1}. {choice.get_name()}" for idx, choice in enumerate(choices))

    def handle_choice(self, choice_index: int):
        commands = self.current_menu.get_commands()
        if 0 <= choice_index < len(commands):
            command = commands[choice_index]
            command.execute(self)
        else:
            print("Invalid choice. Please try again.")
