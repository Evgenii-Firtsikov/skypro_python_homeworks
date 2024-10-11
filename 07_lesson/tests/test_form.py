import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.form_page import FormPage


@pytest.fixture
def driver():
    """Создает экземпляр веб-драйвера Chrome."""
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_submission(driver):
    """Тестирует отправку формы и проверяет классы полей."""
    form = FormPage(driver)
    form.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    form.set_first_name("Иван")
    form.set_last_name("Петров")
    form.set_address("Ленина, 55-3")
    form.set_email("test@skypro.com")
    form.set_phone("+7985899998787")
    form.set_zip_code("")  # Оставляем пустым
    form.set_city("Москва")
    form.set_country("Россия")
    form.set_job_position("QA")
    form.set_company("SkyPro")

    form.submit()

    # Ожидание применения классов
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: "success" in form.get_field_classes("first-name") or
                "danger" in form.get_field_classes("first-name"))

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

    for field, expected_class in expected_classes.items():
        actual_classes = form.get_field_classes(field)
        print(f"Поле {field} имеет классы: {actual_classes}, ожидается наличие класса: {expected_class}")
        assert expected_class in actual_classes, (
            f"Поле {field} имеет классы {actual_classes}, ожидается наличие класса {expected_class}"
        )
