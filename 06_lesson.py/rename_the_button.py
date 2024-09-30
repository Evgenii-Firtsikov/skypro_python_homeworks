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
    driver.get("http://uitestingplayground.com/textinput")

    # Ввод текста в поле
    print("Ввод текста в поле...")
    input_field = driver.find_element(By.ID, 'newButtonName')
    input_field.send_keys("SkyPro")

    # Нажатие на синюю кнопку
    print("Нажатие на кнопку...")
    button = driver.find_element(By.ID, 'updatingButton')
    button.click()

    # Ожидание изменения текста кнопки и получение текста
    print("Ожидание изменения текста кнопки...")
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element((By.ID, 'updatingButton'), "SkyPro")
    )

    # Получение текста и вывод в консоль
    print("Получен текст кнопки: ", driver.find_element(By.ID, 'updatingButton').text)

finally:
    # Закрытие браузера
    print("Закрытие браузера.")
    driver.quit()
