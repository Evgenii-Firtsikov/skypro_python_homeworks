from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SaucedemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Открывает указанную страницу по URL."""
        self.driver.get(url)

    def login(self, username, password):
        """Выполняет вход с указанными именем пользователя и паролем."""
        self.wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

    def add_product_to_cart(self, product_id):
        """Добавляет продукт в корзину по его ID."""
        self.wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    def go_to_cart(self):
        """Переходит в корзину."""
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    def checkout(self):
        """Переходит к процессу оформления заказа."""
        self.wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполняет форму оформления заказа."""
        self.wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        self.driver.find_element(By.ID, 'continue').click()

    def get_total(self):
        """Возвращает итоговую сумму."""
        total_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
        return total_element.text
