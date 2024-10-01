import pytest
from pages.calculator_page import CalculatorPage
from selenium import webdriver


@pytest.fixture
def driver():
    """Создает экземпляр веб-драйвера Chrome."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    """Тестирует калькулятор с заданным задержкой."""
    calculator = CalculatorPage(driver)
    calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator.set_delay(45)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    result = calculator.get_result()
    assert result == "15", f"Ожидалось: 15, но получено: {result}"
