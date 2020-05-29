from flask import Flask
from weather import weather_by_city

import settings

app = Flask(__name__)


@app.route("/")
def index():
    weather = weather_by_city('Moscow', 'Russia', settings.API_KEY)
    if weather:
        return f'The temperature is {weather["temp_C"]} degrees centigrade. It feels like {weather["FeelsLikeC"]}.'
    else:
        return 'The weather forecast is not available now'


if __name__ == "__main__":
    app.run(debug=True)
