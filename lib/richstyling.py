from rich import print
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

def user_input(string):
    text = Text(string)
    text.stylize('green')
    print(text)

def department(string):
    text = Text(string)
    text.stylize('bold blue')
    print(Panel.fit(text))

def menu(string):
    text = Text(string)
    text.stylize('cyan')
    print(Panel.fit(text))

def error(string):
    text = Text(string)
    text.stylize('magenta')
    print(Panel.fit(text))

def qualifier(string):
    text = Text(string)
    text.stylize('yellow')
    print(Panel.fit(text))

def message_to_user(string):
    text = Text(string)
    text.stylize('orange')
    print(Panel.fit(text))

def listing(string):
    pass

def details(string):
    pass
