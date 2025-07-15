## Para evitar errores de importación posibles a la hora de compilar
import sys
import os
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

## Código funcional
from frontend.gui import launch_gui
if __name__ == "__main__":
    launch_gui()