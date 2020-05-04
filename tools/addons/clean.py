import os
import platform

# Clear cmd/teminal
if platform.system() == "Windows":
    os.system("@cls & @title Impulse ToolKit & @color e")
else:
    os.system("clear")
