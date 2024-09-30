from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Импортируем модуль time


# Инициализация драйвера
driver = webdriver.Chrome()


try:
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


    # Заполнение формы с явными ожиданиями
    wait = WebDriverWait(driver, 10)
   
    wait.until(EC.visibility_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
    wait.until(EC.visibility_of_element_located((By.NAME, "last-name"))).send_keys("Петров")
    wait.until(EC.visibility_of_element_located((By.NAME, "address"))).send_keys("Ленина, 55-3")
    wait.until(EC.visibility_of_element_located((By.NAME, "e-mail"))).send_keys("test@skypro.com")
    wait.until(EC.visibility_of_element_located((By.NAME, "phone"))).send_keys("+7985899998787")
    wait.until(EC.visibility_of_element_located((By.NAME, "zip-code"))).send_keys("")  # Оставляем пустым
    wait.until(EC.visibility_of_element_located((By.NAME, "city"))).send_keys("Москва")
    wait.until(EC.visibility_of_element_located((By.NAME, "country"))).send_keys("Россия")
    wait.until(EC.visibility_of_element_located((By.NAME, "job-position"))).send_keys("QA")
    wait.until(EC.visibility_of_element_located((By.NAME, "company"))).send_keys("SkyPro")


    # Нажать кнопку Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    submit_button.click()

 # Список полей и их ожидаемые классы
    expected_classes = {
        "zip-code": "danger",
        "first-name": "success",
        "last-name": "success",
        "address": "success",
        "e-mail": "success",
        "phone": "success",
        "city": "success",
        "country": "success",
        "job-position": "success",
        "company": "success"
    }
    
    # Ожидание 5 секунд после отправки формы
    time.sleep(5)




finally:
    driver.quit()