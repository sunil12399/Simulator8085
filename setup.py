import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        "include_files" : ["Help", "icons"],
        "excludes": "tkinter",
        "replace_paths": [("*", "")]
    }
}

buildOptions = {"replace_paths": [("*", "")]}

executables = [
    Executable('prog.py', base=base)
]

setup(name='8085 Simulator',
      version='0.1',
      description='Sample cx_Freeze PyQt5 script',
      options=options,
      executables=executables, requires=['PyQt5']
      )