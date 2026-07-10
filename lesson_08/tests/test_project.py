import requests

from api.project_api import ProjectAPI
from config import BASE_URL, HEADERS

# Позитивный тест: создание нового проекта


def test_create_project_positive():
    api = ProjectAPI()

    # Отправляем запрос на создание проекта
    response = api.create_project("SkyPro Test Project")

    # Проверяем, что проект успешно создан
    assert response.status_code == 201

    # Получаем тело ответа
    body = response.json()

    # Проверяем, что сервер вернул идентификатор проекта
    assert "id" in body

# Позитивный тест: получение проекта по ID


def test_get_project_positive():
    api = ProjectAPI()

    # Создаем новый проект
    create_response = api.create_project("GET Test Project")
    assert create_response.status_code == 201

    # Сохраняем ID созданного проекта
    project_id = create_response.json()["id"]

    # Получаем информацию о проекте
    get_response = api.get_project(project_id)
    assert get_response.status_code == 200

    body = get_response.json()

    # Проверяем корректность данных проекта
    assert body["id"] == project_id
    assert body["title"] == "GET Test Project"

# Позитивный тест: изменение названия проекта


def test_update_project_positive():
    api = ProjectAPI()

    # Создаем проект
    create_response = api.create_project("Old Project")
    assert create_response.status_code == 201

    project_id = create_response.json()["id"]

    # Изменяем название проекта
    update_response = api.update_project(project_id, "New Project")
    assert update_response.status_code == 200

    # Получаем обновленный проект
    get_response = api.get_project(project_id)
    assert get_response.status_code == 200

    body = get_response.json()

    # Проверяем, что название изменилось
    assert body["title"] == "New Project"

# Негативный тест: создание проекта без обязательного поля title


def test_create_project_negative():
    body = {}

    # Отправляем запрос с пустым телом
    response = requests.post(
        f"{BASE_URL}/projects",
        json=body,
        headers=HEADERS
    )

    # Ожидаем ошибку валидации
    assert response.status_code == 400

# Негативный тест: получение несуществующего проекта


def test_get_project_negative():
    api = ProjectAPI()

    # Используем заведомо несуществующий ID
    response = api.get_project(
        "00000000-0000-0000-0000-000000000000"
    )

    # Проверяем, что сервер возвращает ошибку
    assert response.status_code == 404

# Негативный тест: изменение несуществующего проекта


def test_update_project_negative():
    api = ProjectAPI()

    # Пытаемся изменить проект с несуществующим ID
    response = api.update_project(
        "00000000-0000-0000-0000-000000000000",
        "New Name"
    )

    # Проверяем, что сервер сообщает об отсутствии проекта
    assert response.status_code == 404
