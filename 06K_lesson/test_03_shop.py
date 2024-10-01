from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Настройки для браузера
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Инициализация драйвера Chrome с опциями и использованием webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Шаг 1: Открытие сайта и авторизация
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Шаг 2: Добавление товаров в корзину
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    # Шаг 3: Переход в корзину и нажатие кнопки Checkout
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()

    # Шаг 4: Заполнение формы с данными
    driver.find_element(By.ID, 'first-name').send_keys('Evgenii')
    driver.find_element(By.ID, 'last-name').send_keys('Pupkin')
    driver.find_element(By.ID, 'postal-code').send_keys('123456')
    driver.find_element(By.ID, 'continue').click()

    # Шаг 5: Получение итоговой суммы и вывод в консоль
    wait = WebDriverWait(driver, 10)
    total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
    total_text = total_element.text
    print("Итоговая сумма: ", total_text)

    # Шаг 6: Проверка суммы
    assert total_text == 'Total: $58.29', f"Ожидалось: $58.29, но получено: {total_text}"

finally:
    # Закрытие браузера
    driver.quit()
