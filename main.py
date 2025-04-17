from task import tasks, drafts
import click
from menu import MenuController
from task_service import TaskService
from task import print_list

menu_controller = MenuController(task_service=TaskService(), cli=click)

def main_loop():
    click.echo("Welcome to Task Manager.")
    while True:
        try:
            menu_choice = click.prompt(menu_controller.display_menu())
            print(f"Chosen: {menu_choice}")
            menu_controller.handle_choice(int(menu_choice) - 1)
            print("Current drafts: ")
            print_list(drafts)
            print("Current tasks: ")
            print_list(tasks)
        except click.Abort:
            continue

if __name__ == '__main__':
    main_loop()

    
