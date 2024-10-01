from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_actions(driver):
    try:
        # Переход на страницу
        print(f"Открытие страницы в {driver.name}...")
        driver.get("http://uitestingplayground.com/ajax")

        # Нажатие на кнопку с классом 'btn btn-primary'
        print(f"Нахождение и нажатие на кнопку в {driver.name}...")
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
        button.click()

        # Ожидание появления текста на зеленой плашке с увеличением времени до 30 секунд
        print(f"Ожидание появления зеленой плашки в {driver.name}...")
        wait = WebDriverWait(driver, 30)
        message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success')))

        # Получение текста и вывод в консоль
        print(f"Получен текст из плашки в {driver.name}: {message.text}")

    finally:
        # Закрытие браузера
        print(f"Закрытие {driver.name}.")
        driver.quit()

# Инициализация и выполнение для Google Chrome
chrome_driver = webdriver.Chrome()
chrome_driver.name = "Google Chrome"
perform_actions(chrome_driver)

# Инициализация и выполнение для Firefox
firefox_driver = webdriver.Firefox()
firefox_driver.name = "Firefox"
perform_actions(firefox_driver)

# Инициализация и выполнение для Microsoft Edge
edge_driver = webdriver.Edge()
edge_driver.name = "Microsoft Edge"
perform_actions(edge_driver)
