import sys
import os

# Получаем абсолютный путь к папке '07_lesson'
current_dir = os.path.dirname(os.path.abspath(__file__))

# Добавляем папку '07_lesson' в PYTHONPATH
sys.path.insert(0, current_dir)
