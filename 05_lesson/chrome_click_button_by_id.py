# Импорты
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Настройка опций Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Установка и запуск драйвера с опциями
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

# Зайти на сайт
driver.get("http://uitestingplayground.com/dynamicid")

# Найдите и кликните на кнопку по классу "btn btn-primary"
add_button = driver.find_element(
    By.CSS_SELECTOR, "button.btn.btn-primary"
)

# Клик по кнопке
add_button.click()

# Закрытие браузера
driver.quit()
