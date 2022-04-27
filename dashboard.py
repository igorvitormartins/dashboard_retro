from rich import print
from rich.layout import Layout
from rich.panel import Panel
import time
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
import time
from random import randint
import os
from pygame import mixer
import socket

#funcao para obter nome do host
host = socket.gethostname()

os.system('cls')
acumulo = ''

arq = open("intro\happy.txt")
linhas = arq.readlines()
for linha in linhas:
    print(linha)
    acumulo = acumulo + '\n' + linha
    time.sleep(0.1)
arq.close()

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("May 25, 2018", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
console = Console()
#console.print(table)


titulo = 'Production ISP'
opened = 0
while True:
    if(opened ==0):
        mixer.init()
        mixer.music.load('smb_world_clear.wav')
        mixer.music.play()
    opened = 1
    os.system('cls')
    
    layout = Layout()
    layout.split_column(
        Layout(name="head"),
        Layout(name="up"),
        Layout(name="lower")
    )
    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="center"),
        Layout(name="right"),
    )
    layout["head"].size = 1
    layout["up"].size = 8
    layout["lower"].size = 20
    layout["up"].split(
        Layout(Panel("Hello, [red]" + host + "!", title=titulo, subtitle="Rates and Results")),
        
    )
    layout["right"].split(
        Layout(Panel("Total: 100")),
        Layout(Panel("Total Produzido: 40")),
        Layout(Panel("Restante: 60"))
    )
    layout["left"].split(
        Layout(table)
        
    )
    layout["center"].split(
        Layout(Panel(acumulo))
        
    )
    

    print(layout)
    
    
    time.sleep(5)

