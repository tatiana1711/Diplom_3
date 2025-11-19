import requests
import random
import string
from urls import *

# тестовые данные для основного пользователя
TEST_EMAIL = "Gagarin1204@test.com"
TEST_PASSWORD = "hellospace"
TEST_NAME = "Юра61"

def generate_random_string(length):
    # генерируем случайную строку для создания уникальных пользователей
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def new_user_login_password():
    # генерируем данные для нового пользователя
    login = generate_random_string(10)
    email = f"{login}@example.com"
    password = "password123"
    name = f"TestUser{login}"
    
    return {
        'email': email,
        'password': password,
        'name': name
    }

def create_user_via_api():
    # создаем пользователя через api для тестов
    user_data = new_user_login_password()
    
    response = requests.post(
        API_REGISTER, 
        json=user_data
    )
    
    if response.status_code == 200:
        data = response.json()
        # объединяем данные регистрации с ответом api
        return {
            'email': user_data['email'],
            'password': user_data['password'],
            'name': user_data['name'],
            'accessToken': data.get('accessToken'),
            'refreshToken': data.get('refreshToken'),
            'user': data.get('user', {})
        }
    else:
        print(f"ошибка создания пользователя: {response.status_code}, {response.text}")
        # возвращаем заглушку для тестов
        return {
            'email': user_data['email'],
            'password': user_data['password'],
            'name': user_data['name'],
            'accessToken': None
        }

def delete_user_via_api(access_token):
    # удаляем пользователя через api после тестов
    if access_token:
        headers = {'Authorization': access_token}
        response = requests.delete(
            API_USER,  
            headers=headers
        )
        return response.status_code == 202
    return False