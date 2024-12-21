import os

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Каталог '{directory_path}' был создан")
    else:
        print(f"Каталог '{directory_path}' уже существует")

directory_path = r'D:\Documents\student\Desktop\name'
ensure_directory_exists(directory_path)