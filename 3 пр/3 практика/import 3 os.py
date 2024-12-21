import os
from datetime import datetime

def file_stats(filepath):
    if not os.path.isfile(filepath):
        return {"error": "Файл не найден"}
    
    file_size = os.path.getsize(filepath)
    
    modification_time = os.path.getmtime(filepath)
    formatted_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
    
    file_name, file_extension = os.path.splitext(os.path.basename(filepath))
    
    stats = {
        "size": file_size,
        "last_modified": formatted_time,
        "name": file_name,
        "extension": file_extension,
    }
    
    return stats

if __name__ == "__main__":
    filepath = input("Введите путь к файлу: ")
    stats = file_stats(filepath)
    print(stats)
