from click import prompt as click_prompt, confirm as click_confirm, echo as click_echo, Abort

class AbortException(Abort):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
    

class CliFacade:
    def echo(self, message: str) -> None:
        return click_echo(message)
    
    def prompt(self, message: str) -> str:
        return click_prompt(message)
        
    def confirm(self, message: str) -> bool:
        return click_confirm(message)
