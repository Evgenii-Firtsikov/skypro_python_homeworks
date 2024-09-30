from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Опции для игнорирования SSL-ошибок
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Инициализация драйвера Chrome с опциями
driver = webdriver.Chrome(options=chrome_options)

try:
    # Переход на страницу
    print("Переход на страницу...")
    driver.get("http://uitestingplayground.com/ajax")

    # Нахождение и нажатие на кнопку с классом 'btn btn-primary'
    print("Нахождение и нажатие на кнопку...")
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()

    # Ожидание появления текста на зеленой плашке с увеличением времени до 30 секунд
    print("Ожидание появления зеленой плашки...")
    wait = WebDriverWait(driver, 30)
    message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
    )

    # Получение текста и вывод в консоль
    print("Получен текст из плашки: ", message.text)

finally:
    # Закрытие браузера
    print("Закрытие браузера.")
    driver.quit()
