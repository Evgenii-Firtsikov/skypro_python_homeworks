# Импорты
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

# Настройка FirefoxOptions (если нужно, можно запустить в headless режиме)
options = Options()
# options.add_argument("--headless")  # Если нужен безголовый режим

# Установка и запуск драйвера
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=options
)

# Открытие страницы
driver.get('http://the-internet.herokuapp.com/inputs')

# Найдем поле ввода
input_field = driver.find_element(By.TAG_NAME, 'input')

# Вводим текст "1000"
input_field.send_keys("1000")
sleep(1)  # Для демонстрации действий, можно убрать если не нужно

# Очистим поле
input_field.clear()
sleep(1)  # Для демонстрации действий, можно убрать если не нужно

# Вводим текст "999"
input_field.send_keys("999")
sleep(1)  # Для демонстрации действий, можно убрать если не нужно

# Вывод сообщения для подтверждения
print("Текст '1000' введен, очищен и введен новый текст '999'.")

# Закрытие браузера
driver.quit()
