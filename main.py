from task import tasks, drafts
from menu import MenuController
from task_service import TaskService
from task import print_list
from cli_facade import CliFacade, AbortException

context = {
    "current_draft_id": None
}
cli_facade = CliFacade()
menu_controller = MenuController(task_service=TaskService(), cli=cli_facade, context=context)


def main_loop():
    cli_facade.echo("Welcome to Task Manager.")
    while True:
        try:
            menu_choice = cli_facade.prompt(menu_controller.display_menu())
            print(f"Chosen: {menu_choice}")
            menu_controller.handle_choice(int(menu_choice) - 1)
            print("Current drafts: ")
            print_list(drafts)
            print("Current tasks: ")
            print_list(tasks)
        except AbortException:
            continue

if __name__ == '__main__':
    main_loop()

    
