# Импорты
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

# Настройка FirefoxOptions (например, headless режим, если нужен)
options = Options()
# options.add_argument("--headless")  # Если нужно запускать без интерфейса

# Установка и запуск драйвера
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=options
)

# Открытие страницы
driver.get('http://the-internet.herokuapp.com/login')

# Найдем и заполним поле username
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys('tomsmith')

# Найдем и заполним поле password
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('SuperSecretPassword!')

# Найдем и нажмем кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, '#login > button > i')
login_button.click()

# Вывод сообщения для подтверждения
print("Форма авторизации была успешно отправлена.")

# Закрытие браузера
sleep(3)  # Задержка для проверки результата
driver.quit()
