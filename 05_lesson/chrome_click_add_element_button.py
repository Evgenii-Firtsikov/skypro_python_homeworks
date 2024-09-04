# Импорты
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Установка и запуск драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Зайти на сайт
driver.get(
    "http://the-internet.herokuapp.com/add_remove_elements/"
)

# Пять раз кликните на кнопку "Add Element"
add_button = driver.find_element(By.CSS_SELECTOR, "button")

for _ in range(5):
    add_button.click()

# Соберите со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(
    By.CSS_SELECTOR, "button.added-manually"
)

# Просмотр в консоли результат
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Ожидание для просмотра результата
sleep(5)

# Закрытие браузера
driver.quit()
