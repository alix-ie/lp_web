# WEB project

> This project was made to practice web technologies. It is based on LearnPython course materials,
> but was expanded and improved by @alix-ie.

WEB app extracts python news from `sitepoint.com allows` and allows to view and comment them.

## Installation

(after setup file)

## Configuration

(check for update)

/config.py

```python
from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
WEATHER_API_KEY = 'Your API key'
WEATHER_DEFAULT_CITY = 'City,Country'

SITEPOINT_URL = 'https://www.sitepoint.com'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'web.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'Your secret key'
REMEMBER_COOKIE_DURATION = timedelta(days=5)

REQUESTS_USER_AGENT = 'Your User-Agent'
```

## Launching

(after Dockerfile)