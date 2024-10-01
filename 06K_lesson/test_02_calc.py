from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройки драйвера
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Находим поле с задержкой по ID и очищаем его
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    
    # Вводим значение 45
    delay_input.send_keys("45")

    # Нажимаем на кнопки 7, +, 8 и =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидаем появления результата в окне (15 через 45 секунд)
    result_element = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверяем, что результат равен 15
    assert "15" in driver.find_element(By.CSS_SELECTOR, ".screen").text, "Результат должен быть 15"

finally:
    driver.quit()
