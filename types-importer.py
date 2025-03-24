import os
import re

# Путь к директории с типами
types_dir = "astrobot/types"

# Открываем файл __init__.py для записи
with open(os.path.join(types_dir, "__init__.py"), "w", encoding="utf-8") as init_file:
    # Проходим по всем файлам в директории types
    for filename in os.listdir(types_dir):
        # Игнорируем файл __init__.py и другие не .py файлы
        if filename.endswith(".py") and filename != "__init__.py":
            # Открываем файл для чтения
            with open(os.path.join(types_dir, filename), "r", encoding="utf-8") as type_file:
                # Читаем содержимое файла
                content = type_file.read()
                # Ищем все классы в файле
                classes = re.findall(r"class\s+(\w+)\s*:", content)
                # Если классы найдены, добавляем их в __init__.py
                if classes:
                    for class_name in classes:
                        init_file.write(f"from .{filename[:-3]} import {class_name}\n")
                else:
                    print(f"В файле {filename} не найдено классов.")