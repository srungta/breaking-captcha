from pathlib import Path
import os
import string

def create_folder(folderpath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)

def create_file(filepath):
    if not os.path.isfile(filepath):
        Path(filepath).touch()

def get_filenames_from_folder(folderpath):
    return [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]