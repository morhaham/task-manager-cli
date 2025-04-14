from task import tasks, drafts
import click
from menu import MenuController
from task_service import TaskService

menu_controller = MenuController(task_service=TaskService(), cli=click)

@click.command('create-task-draft')
@click.option("--title", prompt="Task title", help="Task title")
@click.option("--description", prompt="Task description", help="Task description")
def create_task_draft(title, description):
    task = createTaskDraft(title, description)
    click.echo(f"Created task draft for task: {task.state.title}")

def main_loop():
    click.echo("Welcome to Task Manager.")
    while True:
        try:
            menu_choice = click.prompt(menu_controller.display_menu())
            print(f"Chosen: {menu_choice}")
            menu_controller.handle_choice(int(menu_choice) - 1)
        # except CancelFlow:
        #     click.echo("Returning to main menu")
        except click.Abort:
            click.echo("\nExiting gracefully, Bye!")
            break

if __name__ == '__main__':
    main_loop()

    
