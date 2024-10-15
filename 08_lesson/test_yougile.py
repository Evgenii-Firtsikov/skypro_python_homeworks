import pytest
from api import ProjectPage

project_page = ProjectPage()

# Данные для создания проекта
project_data = {
    "title": "SkyPro_DZ",
    "users": {
        "1087ad64-ffbd-413d-b115-362b5a39fd80": "admin"
    }
}

# Позитивные тесты
def test_project_lifecycle():
    # Создаем проект
    response = project_page.create_project(project_data)
    assert response.status_code == 201
    project_id = response.json().get("id")
    assert project_id is not None

    # Получаем список проектов
    response = project_page.get_projects()
    assert response.status_code == 200
    assert any(proj['id'] == project_id for proj in response.json()['content'])

    # Получаем проект по ID
    response = project_page.get_project(project_id)
    assert response.status_code == 200
    assert response.json().get("id") == project_id

    # Удаляем проект
    response = project_page.delete_project(project_id)
    assert response.status_code == 200  # Убедитесь, что проект удален

# Негативные тесты
def test_create_project_invalid_data():
    invalid_data = {
        "title": "",  # Недопустимое название
        "users": {}
    }
    response = project_page.create_project(invalid_data)
    assert response.status_code != 201  # Ожидаем, что проект не будет создан

def test_get_nonexistent_project():
    response = project_page.get_project("invalid_id")
    assert response.status_code == 404  # Ожидаем, что проект не найден

def test_delete_nonexistent_project():
    response = project_page.delete_project("invalid_id")
    assert response.status_code == 404  # Ожидаем, что проект не найден
