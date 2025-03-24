from setuptools import setup, find_packages

# Чтение README.md для описания проекта
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="AstroBot",  # Название вашей библиотеки
    version="0.1.3",  # Версия библиотеки
    author="bsashabbb",  # Ваш username
    description="Асинхронная библиотека для разработки Telegram ботов",  # Краткое описание
    long_description=long_description,  # Длинное описание (обычно из README.md)
    long_description_content_type="text/markdown",  # Тип описания (markdown)
    url="https://github.com/bsashabbb/AstroBot",  # Ссылка на репозиторий
    packages=find_packages(),  # Автоматически находит все пакеты в проекте
    install_requires=[  # Зависимости библиотеки
        "httpx>=0.23.0",  # HTTP-клиент
        "python-dotenv>=0.21.0",  # Для работы с .env (если нужно)
    ],
    classifiers=[  # Классификаторы для PyPI
        "Development Status :: 3 - Alpha",  # Статус разработки
        "Intended Audience :: Developers",  # Целевая аудитория
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  # Лицензия GPLv3
        "Operating System :: OS Independent",  # Кроссплатформенность
    ],
    python_requires=">=3.10",  # Минимальная версия Python
)