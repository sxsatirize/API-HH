import requests
from urllib.parse import urlencode
from datetime import datetime, timedelta

date_to = datetime.now().strftime('%Y-%m-%d')
date_from = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

params = {
    'text': 'кладовщик',
    'area': '1',
    'date_from': date_from,
    'date_to': date_to,
    'no_magic': 'true'
}

headers = {
    "User-Agent": "JobSearcher/1.0 (support@jobsearcher.com)",
    "HH-User-Agent": "JobSearcher/1.0 (support@jobsearcher.com)"
}

try:
    url = 'https://api.hh.ru/vacancies?' + urlencode(params)
    print(f"Отправка запроса на URL: {url}")

    response = requests.get(url, headers=headers)
    print(f"Код ответа: {response.status_code}")
    response.raise_for_status()  

    print("Полный ответ от сервера:")
    print(response.text)

    if response.status_code == 200:
        vacancies = response.json()
        print(f"\nНайдено {vacancies['found']} вакансий в Москве по специальности 'кладовщик' за последний месяц (без учёта гражданства).\n")
        
        for vacancy in vacancies['items']:
            print("=== Вакансия ===")
            print(f"Название: {vacancy['name']}")
            print(f"Компания: {vacancy['employer']['name']}")
            print(f"Город: {vacancy['area']['name']}")
            salary_from = vacancy['salary']['from'] if vacancy['salary'] and 'from' in vacancy['salary'] else 'Не указана'
            salary_to = vacancy['salary']['to'] if vacancy['salary'] and 'to' in vacancy['salary'] else ''
            salary_currency = vacancy['salary']['currency'] if vacancy['salary'] else ''
            print(f"Зарплата: {salary_from} - {salary_to} {salary_currency}")
            print(f"Дата публикации: {vacancy['published_at']}")
            print(f"URL: {vacancy['alternate_url']}\n")
    else:
        print(f"Ошибка: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
