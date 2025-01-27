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

def process_directory(directory: str) -> None:
    """
    Обрабатывает все изображения в указанной директории и её поддиректориях.

    Args:
        directory (str): Путь к директории для обработки.

    Returns:
        None
    """
    for root, _, files in os.walk(directory):
        for file in files:
            # Проверяем расширение файла
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(root, file)
                output_path = os.path.splitext(input_path)[0] + '.heic'
                compress_image(input_path, output_path)
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
def main():
    register_heif_opener()
    user_input: str = input("Введите путь к файлу или директории: ")

    compressor = ImageCompressor() # Создание экземпляра класса
    # Пока ничего не вызываем, только создаем экземпляр

if __name__ == "__main__":
    main()