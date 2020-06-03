import requests
import settings


def weather_by_city(city, country, days=1, lang='en'):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': settings.API_KEY,
        'q': f'{city},{country}',
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
    weather = weather_by_city('Moscow', 'Russia', settings.API_KEY)
    print(weather)
