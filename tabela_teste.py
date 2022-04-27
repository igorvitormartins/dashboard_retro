from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
import time
from random import randint

from rich import print
from rich.highlighter import Highlighter

from rich.progress import Progress
#mensagem = input("INSIRA UMA MENSAGEM: ")
titulo = 'Production ISP'

print(Panel("Hello, [red]my friend!", title=titulo, subtitle="Rates and Results"))

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("May 25, 2018", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)


rainbow = RainbowHighlighter()
print(rainbow("I must not fear. Fear is the mind-killer."))

#print(Panel(console.print(table)))
'''
with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=10)
        progress.update(task2, advance=10)
        progress.update(task3, advance=10)
        time.sleep(1)
'''