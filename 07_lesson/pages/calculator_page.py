from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)  # Увеличенное время ожидания для задержки
    
    def open(self, url):
        """Открывает указанную страницу по URL."""
        self.driver.get(url)
    
    def set_delay(self, delay):
        """Устанавливает задержку в поле ввода."""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))
    
    def click_button(self, button_text):
        """Кликает по кнопке с указанным текстом."""
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']")))
        button.click()
    
    def get_result(self):
        """Получает результат с экрана."""
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
