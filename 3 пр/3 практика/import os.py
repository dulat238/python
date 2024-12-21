import os

def list_files_in_directory(directory_path):
    return[file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

print(list_files_in_directory('D:\\Documents\\student\\Desktop\\task'))