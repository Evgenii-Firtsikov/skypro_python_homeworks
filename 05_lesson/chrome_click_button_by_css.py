# Импорты
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Установка и запуск драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Открытие страницы
driver.get("http://uitestingplayground.com/classattr")

# Ожидание и нахождение синей кнопки по CSS-классу
blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
)

# Клик по синей кнопке
blue_button.click()

# Вывод сообщения в консоль для подтверждения
print("Синяя кнопка была нажата")

# Ожидание 10 секунд, для просмотра результата
sleep(10)

# Закрытие браузера
driver.quit()
