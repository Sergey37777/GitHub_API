import os
import requests
from dotenv import load_dotenv


load_dotenv()

GITHUB_USERNAME = os.getenv('username')
GITHUB_TOKEN = os.getenv('token')
REPO_NAME = os.getenv('repo_name')


API_URL = 'https://api.github.com'


def create_repo():
    """Создать новый публичный репозиторий."""
    url = f'{API_URL}/user/repos'
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
    }
    data = {
        'name': REPO_NAME,
        'private': False,
        'description': 'Test repository'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f'Репозиторий {REPO_NAME} успешно создан.')
    else:
        print(f'Ошибка при создании репозитория: {response.json()}')
    return response


def check_repo_exists():
    """Проверить, существует ли репозиторий."""
    url = f'{API_URL}/users/{GITHUB_USERNAME}/repos'
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
    }
    response = requests.get(url, headers=headers)
    repos = response.json()
    repo_names = [repo['name'] for repo in repos]
    if REPO_NAME in repo_names:
        print(f'Репозиторий {REPO_NAME} найден.')
        return True
    else:
        print(f'Репозиторий {REPO_NAME} не найден.')
        return False


def delete_repo():
    """Удалить репозиторий."""
    url = f'{API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Репозиторий {REPO_NAME} успешно удален.')
    else:
        print(f'Ошибка при удалении репозитория: {response.json()}')


if __name__ == '__main__':
    # Создание репозитория
    create_repo()

    # Проверка наличия репозитория
    if check_repo_exists():
        # Удаление репозитория
        delete_repo()
