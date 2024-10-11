from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url):
        """Открывает указанную страницу по URL."""
        self.driver.get(url)
    
    def set_first_name(self, first_name):
        """Устанавливает имя в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "first-name"))).send_keys(first_name)
    
    def set_last_name(self, last_name):
        """Устанавливает фамилию в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "last-name"))).send_keys(last_name)
    
    def set_address(self, address):
        """Устанавливает адрес в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "address"))).send_keys(address)
    
    def set_email(self, email):
        """Устанавливает электронную почту в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "e-mail"))).send_keys(email)
    
    def set_phone(self, phone):
        """Устанавливает номер телефона в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "phone"))).send_keys(phone)
    
    def set_zip_code(self, zip_code):
        """Устанавливает почтовый индекс в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "zip-code"))).send_keys(zip_code)
    
    def set_city(self, city):
        """Устанавливает город в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "city"))).send_keys(city)
    
    def set_country(self, country):
        """Устанавливает страну в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "country"))).send_keys(country)
    
    def set_job_position(self, job_position):
        """Устанавливает должность в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "job-position"))).send_keys(job_position)
    
    def set_company(self, company):
        """Устанавливает компанию в поле ввода."""
        self.wait.until(EC.visibility_of_element_located((By.NAME, "company"))).send_keys(company)
    
    def submit(self):
        """Отправляет форму."""
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
        submit_button.click()
    
    def get_field_background_color(self, field_name):
        """Получает цвет фона поля."""
        element = self.driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
        return element.value_of_css_property("background-color")
    
    def get_field_classes(self, field_name):
        """Получает классы поля."""
        element = self.driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
        return element.get_attribute("class")
