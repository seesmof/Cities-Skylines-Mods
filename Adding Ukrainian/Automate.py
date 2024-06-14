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
shutil.copy2(
    os.path.join(Current_Dir, "ua.locale"), os.path.join(Target_Path, "ua.locale")
)
