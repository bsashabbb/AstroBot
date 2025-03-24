import os

def collect_files(root_dir, ignore_dirs=None, ignore_extensions=None, ignore_files=None, ignore_self=True, output_file=None):
    """
    Собирает список файлов в проекте, игнорируя указанные папки, расширения, файлы, себя и выходной файл.
    """
    if ignore_dirs is None:
        ignore_dirs = {
            '.venv', 'venv', '.idea', '.git', '__pycache__',  # Виртуальные окружения и кеш
            'node_modules', 'dist', 'build', 'out', 'target', 'bin', 'obj',  # Файлы сборки
            '.vscode', '.vs', '.history', '.pytest_cache', '.mypy_cache',  # Файлы IDE
            'docs', 'tests', 'test', '.github', '.env', 'env',  # Документация, тесты, CI/CD
        }
    if ignore_extensions is None:
        ignore_extensions = {
            # Игнорируемые расширения файлов
            '.iml',  # Файлы IntelliJ IDEA
            '.db', '.sqlite', '.sqlite3', '.sql',  # Базы данных
            # Медиафайлы
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg',  # Изображения
            '.mp3', '.wav', '.ogg', '.flac',  # Аудио
            '.mp4', '.avi', '.mkv', '.mov', '.flv',  # Видео
            '.zip', '.tar', '.gz', '.rar', '.7z',  # Архивы
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',  # Документы
            # Логи и временные файлы
            '.log', '.tmp', '.temp', '.bak',
        }
    if ignore_files is None:
        ignore_files = {
            'Pipfile', 'Pipfile.lock', '.gitignore',  # Файлы зависимостей
            '.DS_Store', 'Thumbs.db', 'desktop.ini',  # Системные файлы
            '.env', '.env.local', '.npmrc', '.yarnrc',  # Файлы конфигурации
            'CHANGELOG.md', 'LICENSE', 'AUTHORS',  # Файлы документации
            'Dockerfile', 'docker-compose.yml',  # Файлы Docker
            'token'
        }

    collected_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Игнорируем ненужные папки
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for filename in filenames:
            # Игнорируем ненужные файлы
            if (filename not in ignore_files and
                    not any(filename.endswith(ext) for ext in ignore_extensions)):
                file_path = os.path.join(dirpath, filename)
                # Игнорируем сам скрипт, если нужно
                if ignore_self and os.path.abspath(file_path) == os.path.abspath(__file__):
                    continue
                # Игнорируем выходной файл, если он указан
                if output_file and os.path.abspath(file_path) == os.path.abspath(output_file):
                    continue
                collected_files.append(file_path)
    return collected_files

def read_files_to_text(file_paths):
    """
    Читает содержимое всех файлов и объединяет их в один текстовый файл.
    """
    combined_text = ""
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_text += f"--- {file_path} ---\n"
                combined_text += file.read() + "\n\n"
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
    return combined_text

def save_text_to_file(text, output_file):
    """
    Сохраняет текстовое описание в файл.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Текстовое описание сохранено в файл: {output_file}")

def main():
    # Указываем текущую папку как корень проекта
    project_dir = os.getcwd()

    # Укажи имя выходного файла
    output_file = 'project_description.txt'

    # Собираем файлы
    files = collect_files(project_dir, ignore_self=True, output_file=output_file)
    print(f"Найдено файлов: {len(files)}")

    # Читаем и объединяем содержимое файлов
    combined_text = read_files_to_text(files)

    # Сохраняем результат в файл
    save_text_to_file(combined_text, output_file)

if __name__ == "__main__":
    main()
