from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройки для браузера
chrome_options = Options()
chrome_options.add_argument("--headless")  # Открыть браузер в фоновом режиме (опционально)

# Инициализация драйвера Chrome с опциями и использованием webdriver_manager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    # Шаг 1: Перейти на сайт
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    # Шаг 2: Дождаться загрузки изображения с ID 'award'
    print("Ожидание загрузки изображения с ID 'award'...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'award'))
    )

    # Шаг 3: Получить значение атрибута src у изображения с ID 'award'
    award_image = driver.find_element(By.ID, 'award')
    award_image_src = award_image.get_attribute('src')

    # Шаг 4: Вывести значение в консоль
    print("Ссылка на изображение с ID 'award': ", award_image_src)

finally:
    # Закрыть браузер
    driver.quit()
