import os

from shutil import move

def sort_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_folder = os.path.join(directory_path, file_extension)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            move(os.path.join(directory_path, filename))

