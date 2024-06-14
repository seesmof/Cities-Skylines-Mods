import os
import shutil
from rich.console import Console
from rich.traceback import install

install()
console = Console()

Target_Path: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "C:\\Program Files\\Epic Games\\CitiesSkylines\\Files\\Locale\\",
)
Current_Dir: str = os.path.dirname(os.path.abspath(__file__))
with console.status("[yellow]Adding Ukrainian locale...[/yellow]"):
    if os.path.exists(os.path.join(Target_Path, "ua.locale")):
        console.print("Ukrainian locale already exists", style="bold cyan")
        exit()
    try:
        shutil.copy2(
            os.path.join(Current_Dir, "ua.locale"),
            os.path.join(Target_Path, "ua.locale"),
        )
        console.print("Added Ukrainian locale", style="bold green")
    except:
        console.print("Failed to add Ukrainian locale", style="bold red")
