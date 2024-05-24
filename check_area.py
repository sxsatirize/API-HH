import requests

headers = {
    'User-Agent': 'MyApp/1.0 (my-app-feedback@example.com)'
}

try:
    response = requests.get('https://api.hh.ru/areas', headers=headers)
    response.raise_for_status()  


    if response.status_code == 200:
        areas = response.json()
        for country in areas:
            if country['id'] == '113': 
                for area in country['areas']:
                    if area['name'].lower() == 'москва':
                        print(f"Код Москвы: {area['id']}")
                        break
    else:
        print(f"Ошибка: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
