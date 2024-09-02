class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """
    
    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
        Пример: `capitalize("skypro") -> "Skypro"`
        """
        return string.lower()  # Ошибка: метод должен возвращать строку с заглавной первой буквой
    
    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        return string  # Ошибка: метод не удаляет пробелы
    
    def to_list(self, string: str, delimiter = ",") -> list[str]:
        """
        Принимает на вход текст с разделителем и возвращает список строк.
        """
        return string.split(" ")  # Ошибка: метод должен использовать заданный разделитель
    
    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ и `False` - если нет
        """
        return symbol in string  # Ошибка: проверка на наличие символа неправильная
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        """
        return string + symbol  # Ошибка: метод добавляет символ, а не удаляет
    
    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
        """
        return string.endswith(symbol)  # Ошибка: метод должен проверять начало строки
    
    def ends_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
        """
        return string.startswith(symbol)  # Ошибка: метод должен проверять конец строки
    
    def is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая и `False` - если нет
        """
        return string != ""  # Ошибка: метод должен проверять, что строка пустая
    
    def list_to_string(self, lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем
        """
        return "".join(lst)  # Ошибка: метод не использует разделитель
