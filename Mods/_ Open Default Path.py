import os

Default_Path: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "C:\\Program Files\\Epic Games\\CitiesSkylines\\Files\\Mods\\",
)
os.startfile(Default_Path)
