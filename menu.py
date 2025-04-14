from typing import List, Protocol
from menu_commands import CreateTask, Exit, ListDrafts, ListTasks, MenuCommand,ReturnToMainMenu
from task import Task, TaskDraft
from task_service import TaskService



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


# class TaskMenu(Menu):
#     def get_commands(self) -> List[MenuCommand]:
#         return [
#             PublishTask(),
#             DeleteTask(),
#         ]
    

class MenuController:
    def __init__(self, task_service: TaskService, cli) -> None:
        self._current_menu = MainMenu()
        self._task_service = task_service
        self._cli = cli

    @property
    def current_menu(self):
        return self._current_menu

    @current_menu.setter
    def current_menu(self, new_current_menu: Menu):
        self._current_menu = new_current_menu

    @property
    def task_service(self):
        return self._task_service

    @property
    def cli(self):
        return self._cli

    def _get_current_menu_commands(self):
        commands_with_return_to_main = self.current_menu.get_commands() + [ReturnToMainMenu()]
        return commands_with_return_to_main

    def display_menu(self) -> str:
        commands = self._get_current_menu_commands()
        return "\n".join(f"{idx + 1}. {choice.get_name()}" for idx, choice in enumerate(commands))

    def handle_choice(self, choice_index: int):
        commands = self._get_current_menu_commands()
        if 0 <= choice_index < len(commands):
            command = commands[choice_index]
            command.execute(self)
        else:
            print("Invalid choice. Please try again.")
