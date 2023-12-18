import requests
from bs4 import BeautifulSoup

'''тут прописана функция которая берёт данные о погоде с сайта wttr'''

def get_weather(city, period='today'):
    base_url = 'https://wttr.in/'
    query = f'{city}?format=%t+%C+%w'

    if period == 'today':
        query += '&today'
    elif period == 'tomorrow':
        query += '&tomorrow'
    elif period == 'week':
        query += '&5'
    elif period == 'month':
        query += '&moon'

    url = base_url + query
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find('span', {'class': 'temperature'}).text
        return f"Прогноз погоды для {city.capitalize()} на {period}: \nТемпература: {temperature}\n{response.text}"
    else:
        return f"Не удалось получить прогноз погоды для {city}"
