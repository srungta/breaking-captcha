import os
from pathlib import Path

def create_folder(folderpath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)

def create_file(filepath):
    if not os.path.isfile(filepath):
        Path(filepath).touch()