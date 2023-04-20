import requests
from flask import current_app


def weather_by_city(city, days=1, lang='en'):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city,
        'format': 'json',
        'num_of_days': f'{days}',
        'lang': lang
    }
    try:
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        current_weather = response.json()
        if 'data' in current_weather:
            if 'current_condition' in current_weather['data']:
                try:
                    return current_weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print('Network error')
        return False
    return False


if __name__ == "__main__":
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    print(weather)
