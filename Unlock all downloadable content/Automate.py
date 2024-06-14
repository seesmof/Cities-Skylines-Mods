import os
import inquirer
from pathlib import Path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

Current_Directory: str = os.path.dirname(os.path.abspath(__file__))
Game_Folder: str = "C:\\Program Files\\Epic Games\\CitiesSkylines"

Does_Game_Folder_Exist: bool = os.path.exists(Game_Folder)
if not Does_Game_Folder_Exist:
    Game_Folder: str = inquirer.prompt(
        [
            inquirer.Text(
                "game folder path",
                message="Please enter the game folder path",
                default="C:\\Program Files\\Epic Games\\CitiesSkylines",
                validate=lambda _, x: x != ""
                and os.path.exists(x)
                and os.path.isdir(x)
                and os.access(x, os.R_OK),
            )
        ]
    )["game folder path"]

Game_Path: Path = Path(Game_Folder)
console.print(Game_Path)
