import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    """Класс для сжатия изображений в формате HEIF."""

    supported_formats = ('.jpg', '.jpeg', '.png') # Поддерживаемые форматы файлов

def __init__(self, quality: int = 50):
        """Инициализация класса с заданным качеством сжатия."""
        self.__quality = quality

def compress_image(self, input_path: str, output_path: str) -> None:
    """Сжимает изображение и сохраняет его в формате HEIF."""
    try:
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality) # Используем self.__quality
        print(f"Сжато: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Ошибка при сжатии {input_path}: {e}")

def process_directory(self, directory: str) -> None:
    """Обрабатывает все изображения в указанной директории и её поддиректориях."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(self.supported_formats):
                input_path = os.path.join(root, file)
                output_path = os.path.splitext(input_path)[0] + '.heic'
                self.compress_image(input_path, output_path) # Вызываем метод compress_image класса
@property
def quality(self) -> int:
        """Геттер для получения значения качества сжатия."""
        return self.__quality

@quality.setter
def quality(self, quality: int) -> None:
        """Сеттер для установки значения качества сжатия."""
        if not (0 <= quality <= 100):
            raise ValueError("Качество должно быть в диапазоне от 0 до 100.")
        self.__quality = quality

def process_input(self, input_path: str) -> None: # Добавляем метод process_input
        """Обрабатывает входной путь и запускает сжатие изображений."""
        input_path = input_path.strip('"') # Удаляем кавычки, если они есть

        if os.path.exists(input_path):
            if os.path.isfile(input_path):
                print(f"Обрабатываем файл: {input_path}")
                output_path = os.path.splitext(input_path)[0] + '.heic'
                self.compress_image(input_path, output_path)
            elif os.path.isdir(input_path):
                print(f"Обрабатываем директорию: {input_path}")
                self.process_directory(input_path)
        else:
            print("Указанный путь не существует")


def main():
    register_heif_opener()
    user_input: str = input("Введите путь к файлу или директории: ")

    compressor = ImageCompressor() # Создание экземпляра класса
    compressor.process_input(user_input) # Вызываем метод process_input экземпляра

if __name__ == "__main__":
    main()
