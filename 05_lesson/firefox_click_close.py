# Импорты
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Настройка FirefoxOptions (например, headless режим, если нужен)
options = Options()
# options.add_argument("--headless")  # Если нужен безголовый режим

# Установка и запуск драйвера
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=options
)

# Открытие страницы
driver.get('http://the-internet.herokuapp.com/entry_ad')

# Ожидаем появления модального окна
wait = WebDriverWait(driver, 10)  # Ждем до 10 секунд
modal = wait.until(
    EC.presence_of_element_located((By.ID, 'modal'))
)

# Ожидаем, пока кнопка "Close" станет кликабельной
close_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='modal-footer']/p[text()='Close']")
    )
)

# Клик по кнопке "Close"
close_button.click()

# Вывод сообщения для подтверждения
print("Кнопка 'Close' была нажата, модальное окно закрыто.")

# Ожидание для просмотра результата
sleep(10)

# Закрытие браузера
driver.quit()
