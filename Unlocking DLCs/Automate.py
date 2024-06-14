import os
import shutil
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
Plugins_Folder: str = os.path.join(Game_Path, "Cities_Data", "Plugins")

New_File_Name: str = "File.dll"
New_File_Path: str = os.path.join(Current_Directory, New_File_Name)
Old_File_Name: str = "EOSSDK-Win64-Shipping.dll"

Does_Old_File_Exist: bool = os.path.exists(os.path.join(Plugins_Folder, Old_File_Name))
if not Does_Old_File_Exist:
    console.print(f"Old file {Old_File_Name} not found", style="bold red")
    exit()

os.rename(
    os.path.join(Plugins_Folder, Old_File_Name),
    os.path.join(Plugins_Folder, Old_File_Name + "_old"),
)
shutil.copy2(New_File_Path, Plugins_Folder)
New_File_Path: str = os.path.join(Plugins_Folder, New_File_Name)
os.rename(
    New_File_Path,
    os.path.join(Plugins_Folder, Old_File_Name),
)
