import requests

from flask import current_app


def get_current_weather(json):
    if 'data' in json and 'current_condition' in json['data']:
        try:
            return json['data']['current_condition'][0]
        except(IndexError, TypeError):
            return False

    return False


def weather_by_city(city, days, lang):
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
        return get_current_weather(response.json())

    except (requests.RequestException, ValueError):
        return False


def display_weather(weather_report):
    if weather_report:
        return f'{weather_report["temp_C"]}\u2103, feels like {weather_report["FeelsLikeC"]}\u2103'
    else:
        'The weather report is not available now'


def get_weather(city, days=1, lang='en'):
    weather_report = weather_by_city(city, days, lang)
    return display_weather(weather_report)
