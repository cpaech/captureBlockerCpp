import PyInstaller.__main__
import PySide6

pysidepath = PySide6.__path__[0]

PyInstaller.__main__.run([
    'blocker.py',
    '--noconfirm',
    '--onefile',
    '--add-data',
    pysidepath + ';./PySide6',
    '-i',
    'NONE'
])