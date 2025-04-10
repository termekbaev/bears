# test_api.py
import pytest
import requests

BASE_URL = "http://localhost:8090"

# Чистим данные перед тестами
@pytest.fixture(autouse=True)
def cleanup():
    yield
    requests.delete(f"{BASE_URL}/bear")

def test_create_black_bear():
    """Тест создания черного медведя с корректными данными"""
    data = {"bear_type": "BLACK", "bear_name": "Timur", "bear_age": 29}
    response = requests.post(f"{BASE_URL}/bear", json=data)
    assert response.status_code == 200
    bear_id = response.text

def test_create_polar_bear():
    """Тест создания полярного медведя с корректными данными"""
    data = {"bear_type": "POLAR", "bear_name": "Anna", "bear_age": 26}
    response = requests.post(f"{BASE_URL}/bear", json=data)
    assert response.status_code == 200
    bear_id = response.text

def test_get_correct_bear():
    """Тест получения созданного медведя"""
    data = {"bear_type": "BROWN", "bear_name": "Browny", "bear_age": 10}
    create_response = requests.post(f"{BASE_URL}/bear", json=data)
    bear_id = create_response.text
    response = requests.get(f"{BASE_URL}/bear/{bear_id}")
    assert response.status_code == 200
    bear = response.json()
    assert bear["bear_type"] == "BROWN"
    assert bear["bear_name"] == "Browny"
    assert bear["bear_age"] == 10

def test_get_incorrect_bear():
    """Тест получения не созданного медведя"""
    bear_id = 777
    response = requests.get(f"{BASE_URL}/bear/{bear_id}")
    assert response.status_code == 404

def test_update_bear():
    """Тест обновления медведя"""
    data = {"bear_type": "BROWN", "bear_name": "Browny", "bear_age": 10}
    create_response = requests.post(f"{BASE_URL}/bear", json=data)
    bear_id = create_response.text
    new_data = {"bear_type": "GUMMY", "bear_name": "Gummy", "bear_age": 2}
    update_response = requests.put(f"{BASE_URL}/bear/{bear_id}", json=new_data)
    assert update_response.status_code == 200
    get_response = requests.get(f"{BASE_URL}/bear/{bear_id}")
    updated_bear = get_response.json()
    assert updated_bear["bear_type"] == "GUMMY"
    assert updated_bear["bear_name"] == "Gummy"

def test_delete_bear():
    """Тест удаления медведя"""
    data = {"bear_type": "BLACK", "bear_name": "Johnny", "bear_age": 3}
    create_response = requests.post(f"{BASE_URL}/bear", json=data)
    bear_id = create_response.text
    delete_response = requests.delete(f"{BASE_URL}/bear/{bear_id}")
    assert delete_response.status_code == 200
    get_response = requests.get(f"{BASE_URL}/bear/{bear_id}")
    assert get_response.status_code == 404

def test_create_invalid_bear_type():
    """Тест создания медведя с некорректным типом"""
    data = {"bear_type": "RED", "bear_name": "Firefox", "bear_age": 10}
    response = requests.post(f"{BASE_URL}/bear", json=data)
    assert response.status_code == 500  # Подсмотрел, что сервис возвращает 500 для невалидных данных

def test_update_nonexistent_bear():
    """Тест обновления медведя"""
    bear_id = 77777
    new_data = {"bear_type": "GUMMY", "bear_name": "Gummy", "bear_age": 2}
    update_response = requests.put(f"{BASE_URL}/bear/{bear_id}", json=new_data)
    assert update_response.status_code == 500

def test_delete_nonexistent_bear():
    """Тест удаления несуществующего медведя"""
    bear_id = 101010
    delete_response = requests.delete(f"{BASE_URL}/bear/{bear_id}")
    assert delete_response.status_code == 404