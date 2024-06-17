import os

Default_Path: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "C:\\Program Files\\Epic Games\\CitiesSkylines\\Files\\Maps\\",
)
os.startfile(Default_Path)
